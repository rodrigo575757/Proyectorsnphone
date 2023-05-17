from django.contrib import admin
from django.urls import path, include
from .views import home,index

urlpatterns = [
    path('',index,name="index"),
    path('paginahome',home,name="home"),
]