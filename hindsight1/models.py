import datetime
from pandas.tseries.offsets import BDay
from random import randint

from django.db import models

from django.contrib.postgres.fields import ArrayField
from django_pandas.io import read_frame
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.utils import timezone

from postgres_copy import CopyManager


class Sp100QuerySet(models.QuerySet):
    
    def random_company(self):
        count = self.all().count()
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def get_tickers(self, number):
        tickers=[]
        for index in range(number):
            t = self.random_company().ticker
            tickers.append(t)
        return tickers  
    
    def get_sector(self, t):
        sector = self.get(ticker=t).sector
        return sector

    def get_industry(self, t):
        industry = self.get(ticker=t).industry
        return industry
   
class Sp100(models.Model):
    ticker = models.CharField(max_length=100, primary_key=True)
    security = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    isin = models.CharField(max_length=100)
    objects = CopyManager()
    playcompanies = Sp100QuerySet.as_manager()
    
    def __str__(self):
        return self.security
 

class PricesQuerySet(models.QuerySet):

    def min_date(self):
        min_date = self.earliest('date').date
        return min_date
    
    def max_date(self):
        max_date = self.latest('date').date
        return max_date
        
    def date_pool(self):
        dates = self.order_by('date').distinct()
        return dates
    
    #start date of play
    def rand_date(self):
        min_date = self.min_date()
        max_date = self.max_date()
        checks = True
        while checks:
            count = self.all().count()
            random_index = randint(0, count - 1)
            rand_date = self.all()[random_index].date
            # Check date has 6M of forward and backwards history
            ret_start = Prices.start_date(rand_date)
            ret_end = Prices.end_date(rand_date)
            if ret_start >= min_date and ret_end <= max_date:
                checks = False
        return rand_date

    def random_company(self, date):
        count = self.filter(date=date).count()
        random_index = randint(0, count - 1)
        return self.filter(date=date)[random_index]

    def get_tickers(self, number, date):
        tickers=[]
        for index in range(number):
            t = self.random_company(date).ticker
            tickers.append(t)
        return tickers  
        
    def start_play(self, number=5):
        checks = 0
        while checks < number:
            date = self.rand_date()
            #get tickers, and check tey are 5 distinct
            while True:
                tickers = self.get_tickers(number=number, date=date)
                if len(set(tickers)) == number:
                    break
            #check if all 5 tickers have 6M forward and trailing data
            start = Prices.start_date(date)
            end = Prices.end_date(date)
            for ticker in tickers:
                try:
                    self.ticker_ror(ticker, start=start, end=date)
                    trailing = True
                except:
                    pass
                    trailing = False
                try:    
                    self.ticker_ror(ticker, start=date, end=end)
                    forward = True
                except:
                    pass
                    forward = False
                if trailing and forward:
                    checks+=1
        return date, tickers
                
                

    def price_ts(self, t, start, end):
        """
        get price TS for a single ticker, from start date to end date
        """
        prices=self.filter(ticker=t).order_by('date')
        df_p=read_frame(prices, fieldnames=['date', 'ticker', 'price'])
        df_p.set_index('date', inplace=True)
        prices_ts=df_p.loc[start:end]
        prices_ts.columns=['ticker', t]
        prices_ts.drop(['ticker'], axis=1, inplace=True)
        return prices_ts
 
    def ticker_ror(self, t, start, end):
        """
        get price datapoint at start and end date, calculate return
        """
        price_t1 = self.get(ticker=t, date=end).price
        price_t0 = self.get(ticker=t, date=start).price
        ror=price_t1/price_t0-1
        return ror


class Prices(models.Model):
    date = models.DateField(null=True)
    ticker = models.CharField(max_length=10)
    price = models.FloatField(default=1.0)
    objects = CopyManager()
    playprices = PricesQuerySet.as_manager()

    def __str__(self):
        return '{} {}'.format(self.ticker, self.date.strftime('%m/%d/%Y'))
    
    #6 month prior date
    def start_date(rand_date):
        ret_start=(rand_date-BDay(130)).date()
        return ret_start
        
    #6 month forward date
    def end_date(rand_date):
        ret_start=(rand_date+BDay(130)).date()
        return ret_start


class PlayRecordQuerySet(models.QuerySet):
    def strategy_ror(self, weights, tickers=None, date=None, play_id=None):
        if play_id != None:
            tickers = self.get(pk=play_id).companies
            date = self.get(pk=play_id).play_rand_date
        rors=[]
        start = date
        end = Prices.end_date(date)
        for ticker in tickers:
            ror = Prices.playprices.ticker_ror(ticker, start, end)
            rors.append(ror)
        strategy_ror = sum([a*b for a,b in zip(weights, rors)])
        return strategy_ror    
    
    def get_past_rors(self, user):
        plays = self.filter(user=user, played=True).order_by('play_time')
        df=read_frame(plays, fieldnames=['strategy_ror', 'play_time'])
        df.set_index('play_time', inplace=True)
        return df

        
    def get_cum_rors(self,user):
        plays = self.filter(user=user, played=True).order_by('play_time')
        df=read_frame(plays, fieldnames=['strategy_ror', 'play_time'])
        df.set_index('play_time', inplace=True)
        df_cum=(1 + df['strategy_ror']).cumprod() - 1
        return df_cum

class PlayRecord(models.Model):
    play_time=models.DateTimeField(default=timezone.now)
    strategy_ror = models.FloatField(default=0.0)
    play_rand_date = models.DateTimeField(default=datetime.datetime.now)
    companies = ArrayField(models.CharField(max_length=10), default=list)
    company_1 = models.FloatField(default=0.0)
    company_2 = models.FloatField(default=0.0)
    company_3 = models.FloatField(default=0.0)
    company_4 = models.FloatField(default=0.0)
    company_5 = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    played = models.BooleanField(default=False)
    objects = PlayRecordQuerySet.as_manager()



class GameInputForm(forms.Form):
    company_1 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min':0, 'max':100, 'step': '5', 'value':0.0}))
    company_2 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min':0, 'max':100, 'step': '5', 'value':0.0}))
    company_3 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min':0, 'max':100, 'step': '5', 'value':0.0}))
    company_4 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min':0, 'max':100, 'step': '5', 'value':0.0}))
    company_5 = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min':0, 'max':100, 'step': '5', 'value':0.0}))



#Extend Django User model to include running capital amount
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    capital = models.FloatField(default=1000000)
    
    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
