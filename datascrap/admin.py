from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Placebet Admin"
admin.site.site_title = "Placebet Admin Portal"
admin.site.index_title = "Welcome To Placebet Database Portal"


# admin.site.unregister(User)
# admin.site.unregister(Group)
    
class Match_master_Admin(admin.ModelAdmin):
    list_display = ["Leauge_id", "date", "Leauge_name", "sports_name", "team1_name", "team2_name", "team1_id", "team2_id", "team1_odds", "team2_odds", "draw_odds"]
admin.site.register(Match_master, Match_master_Admin)
    
class Proxy_master_Admin(admin.ModelAdmin):
    list_display = ["proxy_ip", "proxy_url"]
admin.site.register(Proxy_master, Proxy_master_Admin)

class Arbitrage_master_Admin(admin.ModelAdmin):
    list_display = ["today_date", "today_time", "matchtime", "sports_name", "team1_name", "team2_name", "team1_odds", "team2_odds", "stake1", "stake2", "profit", "profitper"]
admin.site.register(Arbitrage_master, Arbitrage_master_Admin)