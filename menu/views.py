from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')

def samsung(request):
    return render(request,'menu/samsung.html')

def xiaomi(request):
    return render(request,'menu/xiaomi.html')    

def micuenta(request):
    return render(request,'menu/micuenta.html')

def Samsung_galaxy_s10(request):
    return render(request,'menu/Samsung_galaxy_s10.html')

def Xiaomi_redmi_note_12(request):
    return render(request,'menu/Xiaomi_redmi_note_12.html')   

def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html')    








def index(request):
    return render(request,'menu/index.html')

def home(request):
    return render(request,'menu/home.html')

def contacto(request):
    return render(request,'menu/contacto.html')

def borgona(request):
    nombreMascota= "Copito de Nieve"
    edadMascota = 4
    razaMascota = "Pitbull"

    contexto = {
        "datito1": nombreMascota,
        "datito2": edadMascota,
        "datito3": razaMascota
    }

    return render(request,'menu/borgona.html',contexto)


def borgona2(request):
    lista = ["Borgoña","Copito de Nieve","Joselito"]

    contexto = {
        "nombres": lista
    }
    return render(request,'menu/borgona2.html',contexto)