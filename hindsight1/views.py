import pandas as pd
import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import hindsight1.charts.charts as chart
from .models import GameInputForm, Sp100, Prices, PlayRecord, Profile


def ranking(request):
    rank = Profile.objects.all().order_by('-capital')[:10]
    return render(request, 'hindsight1/ranking.html', context={'rank': rank})


@login_required(login_url='/accounts/login/')
def perf_dashboard(request):
    user = request.user
    capital = user.profile.capital
    # previous plays result
    df_plays = PlayRecord.objects.get_past_rors(user)
    past_chart = chart.chart_bar(df_plays['strategy_ror'], title='Performance History',
                               formatchart='.1%', categories=None, size=(500,500))
    # cumulate returns
    df_cum = PlayRecord.objects.get_cum_rors(user)
    df_capital = (df_cum+1)*1000000
    cum_chart=chart.chart_bar_cum(df_capital, df_cum, title='Cumulate Returns',
                                  categories=False, formatchart='$,.0f', size=(500,500))

    context = {
        'user': user,
        'past_chart': past_chart,
        'cum_chart': cum_chart,
        'capital': capital,
    }
    return render(request, 'hindsight1/performance.html', context)


def result(request):
    weights = request.session['weights'] 
    companies = request.session['companies']
    year = request.session['year']
    month = request.session['month']
    day = request.session['day']
    date = datetime.date(year, month, day)
    user = request.user
    port_ror = PlayRecord.objects.strategy_ror(weights, tickers=companies, date=date)
    if user.is_authenticated:
        play_id = request.session['play_id']
        user.profile.capital = user.profile.capital*(1+port_ror)
        user.save()
        play_object = PlayRecord.objects.get(pk=play_id)
        play_object.strategy_ror = port_ror
        play_object.played = True
        play_object.save()
    end = Prices.end_date(date)
    prices = pd.DataFrame()
    for company in companies:
        prices_t = Prices.playprices.price_ts(company, date, end)
        prices = pd.concat([prices, prices_t], axis=1)
    strat_ts = strategy_ts(prices, weights)
    strat_cum = chart.chart_line(strat_ts, formatchart='.3%', name='Strategy Performance', size=[600,400])
    names=[]
    rors=[]
    for ticker in companies:
        name = Sp100.objects.get(pk=ticker).security
        names.append(name)
        ror = Prices.playprices.ticker_ror(ticker, date, end)
        ror = '{:.2%}'.format(ror)
        rors.append(ror)
    return render(request,
                  'hindsight1/result.html',
                  context={'port_ror':port_ror,
                           'weights': weights,
                           'tickers': companies,
                           'date': date,
                           'strat_cum': strat_cum,
                           'names': names,
                           'rors': rors,
                           'user': user,
                           }
                  )
    
def play(request):
    #GameInputFormSet = formset_factory(GameInputForm, extra=5)
    if request.method == 'POST':
        #formset = GameInputFormSet(request.POST)
        form = GameInputForm(request.POST)
        #if formset.is_valid():
        if form.is_valid():
            weights=[]
            w1=form.cleaned_data.get('company_1')/100
            w2=form.cleaned_data.get('company_2')/100
            w3=form.cleaned_data.get('company_3')/100
            w4=form.cleaned_data.get('company_4')/100
            w5=form.cleaned_data.get('company_5')/100
            weights=[w1,w2,w3,w4,w5]
            #play_id = request.POST.get("play_id","")
            #save data into session and send to result view
            #request.session['play_id'] = request.POST.get("play_id","")
            request.session['weights'] = weights
            
            return HttpResponseRedirect(reverse('hindsight1:result'))
        else:
            HttpResponseRedirect(reverse('hindsight1:play'))
    else:
        #get user and current capital
        user = request.user
        #Instantiate a new play
        date, tickers = Prices.playprices.start_play(number=5)
        start = Prices.start_date(date)
        if user.is_authenticated:
            play = PlayRecord(play_rand_date=date, companies=tickers)
            play.user = user
            play.save()
            request.session['play_id'] = play.id
        #Store play info into session to pass into next view.
        request.session['companies'] = tickers
        #must save date info in session as integers, as datetimes cannot be
        #serialized by json
        request.session['year'] = date.year
        request.session['month'] = date.month
        request.session['day'] = date.day
        form=GameInputForm()
        prices=pd.DataFrame()
        data = {}
        col_names = ['Company 1', 'Company 2', 'Company 3', 'Company 4', 'Company 5']
        for idx, company in enumerate(tickers):
            data[col_names[idx]]={}
            prices_t=Prices.playprices.price_ts(company, start, date)
            prices=pd.concat([prices, prices_t], axis=1)
            data[col_names[idx]]['sector']=Sp100.playcompanies.get_sector(company)
            data[col_names[idx]]['industry']=Sp100.playcompanies.get_industry(company)
            
            
        prices.columns = col_names
        chart_div=chart.chart_line_base100(prices, formatchart='.2f', title='Price Return (rebased to 100)', size=[600,400])

            
        return render(request, 'hindsight1/playV5.html', context={'form': form,
                                                                #'play_id':play_id,
                                                                'chart_div': chart_div,
                                                                'user': user,
                                                                'data': data,
                                                                }
                    )        


def strategy_ts(prices, weights):
    rors=prices.pct_change(periods=1).fillna(value=0)
    strategy=rors.dot(weights)
    cum = pd.DataFrame((1+strategy).cumprod()-1, columns=['strategy'])
    return cum


