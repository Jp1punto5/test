from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Usuarios
import sqlite3
from django.conf import settings
# Create your views here.
# creacion de funciones que se podran llamar para invocar las ventanas

def index(request):
    context={}
    return render(request, 'proyect_1/index.html', context)

def menu2(request):
    if request.method == "POST":
        usuario2 = request.POST.get("txtUser", "").strip()
        password2 = request.POST.get("txtPass", "").strip()
        if usuario2 == '' or password2 == '':
            error = 'no se aceptan campos vacios'
            return render( request,'proyect_1/index.html',{'error_message':error})
        else:
           try:              
                usuario = Usuarios.objects.get(usu_user= usuario2, usu_clave = password2)
                msg = 'Bienvenido ' + usuario.usu_user
                return render(request,'proyect_1/menu2.html',{'msg':msg})
           except Usuarios.DoesNotExist:
               msg = 'Las Credenciales de Acceso ingresadas no coinciden, vuelva a intentarlo'
               return render( request,'proyect_1/index.html',{'error_message':msg})
    else:
        error = 'No puede ingresar sin credenciales de Acceso'
        return render(request,'proyect_1/index.html',{'error_message':error})




def mostrar(request):
    clavesLista = Usuarios.objects.all()
    return render(request,'proyect_1/mostrar.html',{'claves': clavesLista})


        

