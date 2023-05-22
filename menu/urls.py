from django.contrib import admin
from django.urls import path, include
from .views import principal, samsung, xiaomi, Xiaomi Redmi Note 12, Samsung Galaxy S10 home, registro, cambiarcontra, index, contacto, borgona, borgona2

urlpatterns = [
    path('',principal,name="principal"),
    path('samsung',samsung,name="samsung"),
    path('micuenta',xiaomi,name="micuenta"),
    path('Xiaomi Redmi Note 12',Xiaomi Redmi Note 12,name="Xiaomi Redmi Note 12"),
    path('Samsung Galaxy S10',Samsung Galaxy S10,name="Samsung Galaxy S10"),
    path('cambiarcontra',cambiarcontra,name="cambiarcontra"),
    path('registro',registro,name="registro"),


    path('index',index,name="index"),
    path('home',home,name="home"),
    path('contacto',contacto,name="contacto"),
    path('borgona',borgona,name="borgona"),
    path('borgona2',borgona2,name="borgona2"),
]