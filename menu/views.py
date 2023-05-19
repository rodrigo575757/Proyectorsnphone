from django.shortcuts import render

# Create your views here.
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