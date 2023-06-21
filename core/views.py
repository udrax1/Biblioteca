from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.decorators import csrf
from .models import Usuario,Horario,Sala
from .forms import UsuarioForm
import requests
import json

# Create your views here.
def login(request):
    return render(request, '/accounts/login/')

def inicio(request):
    return render(request, 'inicio.html')



def horarios(request):
     with open('db.json') as json_file:
        data = json.load(json_file)
    
     return render(request, 'horarios.html', {'data': data})



def salas(request):
    return render(request, 'salas.html')




def form_usuarios(request):
    if request.method=='POST':
        usuario_form = UsuarioForm(request.POST ,request.FILES)
        if usuario_form.is_valid():
            usuario_form.save()
            messages.success(request, "Se ingreso el Usuario correctamente.")
            return redirect('usuarios')
    else:
        usuario_form= UsuarioForm()
    return render(request, 'form_usuarios.html', {'usuario_form': usuario_form})



def usuarios(request):
    usuarios = Usuario.objects.all() #traigo todos los objetos de la clase Producto y los almaceno en 
    datosUsuarios = {
        'usuarios': usuarios  #diccionario para llamarlo desde el html
    }
    return render (request, 'usuarios.html', datosUsuarios)


def eliminar_usuarios(request, id):
    usuarios= Usuario.objects.get(rut=id)
    usuarios.delete()
    messages.success(request, "El usuario fue eliminado correctamente.")
    return redirect("usuarios")

def mod_usuarios(request, id):
    usuario = Usuario.objects.get(rut=id)
    datos = {'form': UsuarioForm(instance=usuario)}
    
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        
        if formulario.is_valid():
            formulario.fields_to_exclude = ['contraseña', 'contraseña2']
            formulario.save()  # lo sobreescribe
            messages.success(request, "El usuario fue modificado correctamente.")
            return redirect('usuarios')
    
    return render(request, 'mod_usuario.html', datos)