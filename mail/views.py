from django.shortcuts import render, redirect, HttpResponse
from datascrap.models import *
from datetime import datetime
import json, os, random, requests

def arbitrage(request):
    for row in list(Match_master.objects.all().values()):
        team1_odds = float(row['team1_odds'])
        team2_odds = float(row['team2_odds'])
        stake = 100
        stake1 = stake / (1 + (team1_odds / team2_odds))
        stake2 = stake / (1 + (team2_odds / team1_odds))
        payout1 = stake1 * team1_odds
        payout1 = round(payout1 , 2)
        totalprofite = payout1 - stake
        totalprofite = round(totalprofite,2)
        if totalprofite < 0:
            totalprofiteper=(totalprofite*100)/stake
            stake1 = round(stake1 , 2)
            stake2 = round(stake2 , 2)
            totalprofite = round(totalprofite , 2)
            totalprofiteper = round(totalprofiteper , 2)
            Arbitrage_master.objects.create(today_date = datetime.now().date(), today_time = datetime.now().time(), matchtime = row['date'], sports_name = row['sports_name'], team1_name = row['team1_name'], team2_name = row['team2_name'], team1_odds = row['team1_odds'], team2_odds = row['team2_odds'], stake1 = stake1, stake2 = stake2, profit = totalprofite, profitper = totalprofiteper)
    return HttpResponse('200')



        
