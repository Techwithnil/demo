from django.db import models

class Match_master(models.Model):
    Leauge_id = models.IntegerField()
    date = models.TextField()
    Leauge_name = models.TextField()
    sports_name = models.TextField()
    team1_name = models.TextField()
    team2_name = models.TextField()
    team1_id = models.IntegerField(default = None, null = True)
    team2_id = models.IntegerField(default = None, null = True)
    team1_odds = models.TextField(default = None, null = True)
    team2_odds = models.TextField(default = None, null = True)
    draw_odds = models.TextField(default = None, null = True)
    class Meta:
        db_table='match_master'
        verbose_name_plural ='match_master'
        unique_together = ("date", "Leauge_name", "sports_name", "team1_name", "team2_name", "team1_id", "team2_id")

class Proxy_master(models.Model):
    proxy_ip = models.CharField(max_length=150, default = None, null = True, unique = True)
    proxy_url = models.TextField(default = None, null = True)
    class Meta:
        db_table='proxy_master'
        verbose_name_plural ='proxy_master'

class Arbitrage_master(models.Model):
    today_date = models.DateField()
    today_time = models.TimeField()
    matchtime = models.TextField()
    sports_name = models.TextField()
    team1_name = models.TextField()
    team2_name = models.TextField()
    team1_odds = models.TextField(default = None, null = True)
    team2_odds = models.TextField(default = None, null = True)
    stake1 = models.DecimalField(max_digits=15, decimal_places=2)
    stake2 = models.DecimalField(max_digits=15, decimal_places=2)
    profit = models.DecimalField(max_digits=15, decimal_places=2)
    profitper = models.DecimalField(max_digits=15, decimal_places=2)
    class Meta:
        db_table='arbitrage_master'
        verbose_name_plural ='arbitrage_master'

  
  
  
  
  
  
  




