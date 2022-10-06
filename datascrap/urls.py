
from django.urls import path
from . import views
urlpatterns = [
    path('datascrap/',views.datascrap,name='datascrap'),
    path('proxy_setup/',views.proxy_setup,name='proxy_setup'),
]


