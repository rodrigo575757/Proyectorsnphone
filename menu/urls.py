from django.contrib import admin
from django.urls import path, include
from .views import principal, samsung, xiaomi, Xiaomi_redmi_note_12, Samsung_galaxy_s10, registro, cambiarcontra, index,home, contacto, borgona, borgona2

urlpatterns = [
    path('',principal,name="principal"),
    path('samsung',samsung,name="samsung"),
    path('micuenta',xiaomi,name="micuenta"),
    path(' Xiaomi_redmi_note_12', Xiaomi_redmi_note_12,name=" Xiaomi_redmi_note_12"),
    path('Samsung_galaxy_s10',Samsung_galaxy_s10,name="Samsung_galaxy_s10"),
    path('cambiarcontra',cambiarcontra,name="cambiarcontra"),
    path('registro',registro,name="registro"),


    path('index',index,name="index"),
    path('home',home,name="home"),
    path('contacto',contacto,name="contacto"),
    path('borgona',borgona,name="borgona"),
    path('borgona2',borgona2,name="borgona2"),
]