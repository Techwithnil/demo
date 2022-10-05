from django.urls import path
from . import views

urlpatterns = [
    path('arbitrage', views.arbitrage, name='arbitrage'),
]




