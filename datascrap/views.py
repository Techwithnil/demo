from difflib import Match
import os, sys, json, ssl, smtplib, random, requests
from bs4 import BeautifulSoup
from django.shortcuts import render, HttpResponse
from time import sleep
from datetime import datetime
from dateutil import tz
from dotenv import load_dotenv
from .models import *
load_dotenv()
prx = requests.Session()



def proxy():
    li=list()
    url='https://free-proxy-list.net/'
    page=requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    value = soup.find(class_="modal-body")
    value=value.text
    data=value.split('\n')
    data.reverse()
    data.pop()
    data.pop()
    for i in range(len(data)):
        n=data[i]
        if n != '':
          link='https://{}'.format(n)
          li.append(link)   
    return li 
  
def location(ip_address):
  try:
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print(result)
  except:
    pass

def proxy_setup(request):
    li=proxy()
    for c in li:
        print(c)
        n=c.split('//')[1].split(':')[0]
        try:
            Proxy_master.objects.create(proxy_ip = n, proxy_url = c)
        except:pass
    return HttpResponse('200')
    

def comeonbet():
    link=random.choice(list(Proxy_master.objects.all().values()))['proxy_url']
    url = 'https://nodeprm.tsports.online/cache/48/en/in/Asia-Kolkata/init/34/welcome-popular.json'
    prx.proxies = {"http": '{}'.format(link)}
    data = prx.get(url).json()
    for i in data['events']:
        Leauge_id = i['tournament_id']
        date = i['date_start']
        Leauge_name = i['tournament_name']
        sports_name = i['sport_title']
        s = i['main_odds']['main']
        try:
            news = list(s.keys())
            team1_name = i["teams"]["home"]
            team2_name = i["teams"]["away"]
            team = i['main_odds']['main']
            team1_id = i['main_odds']['main'][str(news[0])]['id']
            team2_id = i['main_odds']['main'][str(news[1])]['id']
            if len(team) == 3:
                team1_odds = i['main_odds']['main'][str(news[0])]['odd_value']
                draw_odds = i['main_odds']['main'][str(news[1])]['odd_value']
                team2_odds = i['main_odds']['main'][str(news[2])]['odd_value']
            else:
                team1_odds = i['main_odds']['main'][str(news[0])]['odd_value']
                team2_odds = i['main_odds']['main'][str(news[1])]['odd_value']
                draw_odds = None
        except:
            pass
        try:
            Match_master.objects.create(Leauge_id = Leauge_id, date = date, Leauge_name = Leauge_name, sports_name = sports_name, team1_name = team1_name, team2_name = team2_name, team1_id = team1_id, team2_id = team2_id)
        except:pass
        match_id = list(Match_master.objects.filter(Leauge_id = Leauge_id).filter(date = date).filter(Leauge_name = Leauge_name).filter(sports_name = sports_name).filter(team1_name = team1_name).filter(team2_name = team2_name).filter(team1_id = team1_id).filter(team2_id = team2_id).values())[0]['id']
        Match_master.objects.filter(id = match_id).update(team1_odds = team1_odds)
        Match_master.objects.filter(id = match_id).update(team2_odds = team2_odds)
        Match_master.objects.filter(id = match_id).update(draw_odds = draw_odds)
        
def datascrap(request):
    comeonbet()
    return HttpResponse('200')
