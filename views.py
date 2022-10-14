import os, sys, json, ssl, smtplib, random, requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
import sqlite3
prx = requests.Session()
sqliteConnection = sqlite3.connect('Arbitrage.db')
cursor = sqliteConnection.cursor()


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
    except:pass

def proxy_setup():
    li=proxy()
    for c in li:
        n=c.split('//')[1].split(':')[0]
        sqlitein = "INSERT INTO Proxy_master(proxy_ip, proxy_url)  VALUES ('{}', '{}')".format(n, c)
        count = cursor.execute(sqlitein)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)

def comeonbet():
    cursor.execute("SELECT proxy_url FROM Proxy_master")
    sqliteConnection.commit()
    link = random.choice(cursor.fetchall())[0]
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
        sqlitein = "REPLACE INTO Match_master(Leauge_id, date, Leauge_name, sports_name, team1_name, team2_name, team1_id, team2_id, team1_odds, team2_odds, draw_odds)  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Leauge_id, date, Leauge_name, sports_name, team1_name, team2_name, team1_id, team2_id ,team1_odds, team2_odds, draw_odds)
        count = cursor.execute(sqlitein)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)



def arbitrage():
    cursor.execute("SELECT * FROM Match_master")
    sqliteConnection.commit()
    # (255555, '2022-10-09T08:10:00.000Z', 'Twenty20 International', 'Cricket', 'Australia', 'England', 728968439, 728968440, None, None, None)
    for row in cursor.fetchall():
        team1_odds = float(row[-3])
        team2_odds = float(row[-2])
        stake = 100
        stake1 = stake / (1 + (team1_odds / team2_odds))
        stake2 = stake / (1 + (team2_odds / team1_odds))
        payout1 = stake1 * team1_odds
        payout1 = round(payout1 , 2)
        totalprofite = payout1 - stake
        totalprofite = round(totalprofite,2)
        totalprofiteper=(totalprofite*100)/stake
        stake1 = round(stake1 , 2)
        stake2 = round(stake2 , 2)
        totalprofite = round(totalprofite , 2)
        totalprofiteper = round(totalprofiteper , 2)
        sqlitein = "REPLACE INTO Arbitrage_master(today_date, today_time, matchtime, sports_name, team1_name, team2_name, team1_odds, team2_odds, stake1, stake2, profit, profitper)  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(datetime.now().date(), datetime.now().time(), row[2], row[4], row[5], row[6], team1_odds, team2_odds, stake1, stake2, totalprofite, totalprofiteper)
        count = cursor.execute(sqlitein)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)



# proxy_setup()
comeonbet()
arbitrage()
# cursor.close()
while True:
    comeonbet()
    arbitrage()