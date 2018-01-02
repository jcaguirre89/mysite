from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import GameInputForm, Sp100, Prices, PlayRecord, Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory
from django.urls import reverse
import numpy as np
import hindsight1.charts.charts as chart
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from hindsight1.stock_data import get_data





# Create your views here.
#def index(request):
#    return render(request, 'hindsight1/index_h1.html')


"""
class IndexView(generic.DetailView):
    template_name = 'hindsight1/index.html'
"""
   

def ranking(request):
    rank=Profile.objects.all().order_by('-capital')[:10]
    return render(request,
           'hindsight1/ranking.html',
           context={'rank': rank,
                    }
           )
    
#def show_data(request):
#    ticker = request.GET.get('company', None)
 #   data = get_data(ticker)


@login_required(login_url='/accounts/login/')
def perf_dashboard(request):
    user = request.user
    capital = user.profile.capital
    #previous plays result
    df_plays = PlayRecord.recobjects.get_past_rors(user)
    past_chart=chart.chart_bar(df_plays['strategy_ror'], title='Performance History', formatchart='.1%', categories=False, size=[500,500])    
    #cumulate returns
    df_cum = PlayRecord.recobjects.get_cum_rors(user)
    df_capital = (df_cum+1)*1000000
    cum_chart=chart.chart_bar_cum(df_capital, df_cum, title='Cumulate Returns', categories=False, formatchart='$,.0f', size=[500,500])
  
    return render(request, 
                  'hindsight1/performance.html',
                  context={
                          'user': user,
                          'past_chart': past_chart,
                          'cum_chart': cum_chart,
                          'capital': capital,
                          #'title': 'Play by play performance',
                          }
                  )

@login_required(login_url='/accounts/login/')
def result(request):
    play_id = request.session['play_id']
    weights = request.session['weights'] 
    user = request.user
    capital_pre = user.profile.capital
    port_ror = PlayRecord.recobjects.strategy_ror(play_id, weights)
    capital_post = capital_pre*(1+port_ror)
    user.profile.capital = capital_post
    user.save()
    play = PlayRecord.recobjects.get(pk=play_id)
    tickers = play.companies
    play.strategy_ror = port_ror
    play.played = True
    play.save()
    #create cumulate return chart for strategy
    date = play.play_rand_date
    end = Prices.end_date(date)
    prices=pd.DataFrame()
    for company in tickers:
        prices_t=Prices.playprices.price_ts(company, date.date(), end)
        prices=pd.concat([prices, prices_t], axis=1)
        
    strat_ts=strategy_ts(prices, weights)
    strat_cum=chart.chart_line(strat_ts, formatchart='.3%', name='Strategy Performance', size=[600,400])
    #company returns for result table
    names=[]
    rors=[]
    for ticker in tickers:
        name=Sp100.objects.get(pk=ticker).security
        names.append(name)
        ror=Prices.playprices.ticker_ror(ticker, date.date(), end)
        ror='{:.2%}'.format(ror)
        rors.append(ror)
    return render(request,
                  'hindsight1/result.html',
                  context={'port_ror':port_ror,
                           'weights': weights,
                           'tickers': tickers,
                           'date': date,
                           'strat_cum': strat_cum,
                           'names': names,
                           'rors': rors,
                           'user': user,
                           'capital': capital_post,
                           }
                  )
    
@login_required(login_url='/accounts/login/')
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
            play_id = request.POST.get("play_id","")
            #save data into session and send to result view
            request.session['play_id'] = request.POST.get("play_id","")
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
        play = PlayRecord(play_rand_date=date, companies=tickers)
        play.user = user
        play.save()
        #Get play id, which will be passed back in the form when it's bound
        #to know how to identify the play
        play_id=play.id
        form=GameInputForm()
        prices=pd.DataFrame()
        data = {}
        for company in tickers:
            data[company]={}
            prices_t=Prices.playprices.price_ts(company, start, date)
            prices=pd.concat([prices, prices_t], axis=1)
            data[company]['sector']=Sp100.playcompanies.get_sector(company)
            data[company]['industry']=Sp100.playcompanies.get_industry(company)
        prices.columns = ['Company 1', 'Company 2', 'Company 3', 'Company 4', 'Company 5']
        chart_div=chart.chart_line_dropdown(prices, formatchart='$.2f', name='Price', size=[600,400])

            
        return render(request, 'hindsight1/playV5.html', context={'form': form,
                                                                'play_id':play_id,
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


