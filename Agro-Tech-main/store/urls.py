from django.contrib import admin
from django.urls import path
from .views import etrade, index

urlpatterns = [
    path('',index,name='homepage'),
    path('etrade',etrade, name='etradpage'),
]
