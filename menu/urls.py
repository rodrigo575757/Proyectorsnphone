from django.contrib import admin
from django.urls import path, include
from .views import principal,samsung,xiaomi,home,index, contacto, borgona, borgona2

urlpatterns = [
    path('',principal,name="princial")
    path('samsung',samsung,name="samsung")
    path('xiaomi',xiaomi,name="xiaomi")
    path('index',index,name="index"),
    path('home',home,name="home"),
    path('contacto',contacto,name="contacto"),
    path('borgona',borgona,name="borgona"),
    path('borgona2',borgona2,name="borgona2"),
]