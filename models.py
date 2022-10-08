import sqlite3
connection_obj = sqlite3.connect('Arbitrage.db')
cursor_obj = connection_obj.cursor()
def match():
    table = """ CREATE TABLE Match_master( Leauge_id  INT, date  VARCHAR(255) NOT NULL, Leauge_name  VARCHAR(150) NOT NULL, sports_name  VARCHAR(100) NOT NULL, team1_name  VARCHAR(150) NOT NULL, team2_name  VARCHAR(150) NOT NULL, team1_id  INT, team2_id  INT, team1_odds  VARCHAR(50) NULL, team2_odds  VARCHAR(50) NULL, draw_odds  VARCHAR(50) NULL, UNIQUE(Leauge_id, date, Leauge_name, sports_name, team1_name, team2_name, team1_id, team2_id)); """
    cursor_obj.execute(table)
    print("Table is Match_master Ready")

def porxy():
    table = """ CREATE TABLE Proxy_master( proxy_ip  VARCHAR(150) NOT NULL UNIQUE, proxy_url  VARCHAR(150) NOT NULL); """
    cursor_obj.execute(table)
    print("Table is Proxy_master Ready")

def arbitrage():
    table = """ CREATE TABLE Arbitrage_master(today_date  VARCHAR(150) NOT NULL, today_time VARCHAR(150) NOT NULL, matchtime VARCHAR(150) NOT NULL, sports_name VARCHAR(150) NOT NULL, team1_name VARCHAR(150) NOT NULL, team2_name VARCHAR(150) NOT NULL, team1_odds VARCHAR(150) NOT NULL, team2_odds VARCHAR(150) NOT NULL, stake1  VARCHAR(150) NOT NULL, stake2  VARCHAR(150) NOT NULL, profit VARCHAR(150) NOT NULL, profitper VARCHAR(150) NOT NULL); """
    cursor_obj.execute(table)
    print("Table is Arbitrage_master Ready")
    
match()
porxy()
arbitrage()
connection_obj.close()
