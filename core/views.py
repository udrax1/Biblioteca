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
    response = requests.get('http://localhost:3000/salas')
    data = response.json()
    if request.method == 'PUT':
        horario_id = request.POST.get('horario_id')
        nuevo_estado = request.POST.get('nuevo_estado')


        response = requests.put(f'http://localhost:3000/salas/{horario_id}', json={'reservada': nuevo_estado})
        data = response.json()

        
    return render(request, 'horarios.html', {'data': data})



def form_usuarios(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, request.FILES)
        if usuario_form.is_valid():
            usuario_form.save()
            messages.success(request, "Se ingresó el Usuario correctamente.")
            return redirect('usuarios')
    else:
        usuario_form = UsuarioForm()
    
    response = requests.get('http://localhost:3300/usuario')
    data = response.json()
    
    if request.method == 'POST':
        # Obtener los datos ingresados en el formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        password = request.POST.get('pass')
        repassword = request.POST.get('repass')
        bloqueado = request.POST.get('bloqueado')
        
        # Crear un diccionario con los datos del nuevo usuario
        nuevo_usuario = {
            'nombre': nombre,
            'apellidos': apellidos,
            'correo': correo,
            'pass': password,
            'repass': repassword,
            'bloqueado': bloqueado
        }
        
        # Realizar una solicitud POST al servidor JSON
        post_response = requests.post('http://localhost:3300/usuario', json=nuevo_usuario)
        
        if post_response.status_code == 201:
            messages.success(request, "Se ingresó el Usuario correctamente mediante POST.")
            return redirect('usuarios')
        else:
            messages.error(request, "Error al ingresar el Usuario mediante POST.")
    
    return render(request, 'form_usuarios.html', {'usuario_form': usuario_form, 'data': data})



def usuarios(request):
    response = requests.get('http://localhost:3300/usuario')
    data = response.json()
    return render(request, 'usuarios.html', {'data': data})


def eliminar_usuarios(request, usuario_id):
    url = f'http://localhost:3300/usuario/{usuario_id}'

    response = requests.delete(url)

    if response.status_code == 200:
        messages.success(request, "El usuario ha sido eliminado correctamente.")
    else:
        messages.error(request, "No se pudo eliminar el usuario.")

    return redirect('usuarios')

def mod_usuarios(request, id):
    url = f'http://localhost:3300/usuario/{id}'
    response = requests.get(url)
    usuario_data = response.json()

    if request.method == 'POST':
        usuario_data['nombre'] = request.POST.get('nombre')
        usuario_data['apellidos'] = request.POST.get('apellidos')
        usuario_data['correo'] = request.POST.get('correo')
        usuario_data['pass'] = request.POST.get('pass')
        usuario_data['repass'] = request.POST.get('repass')
        usuario_data['bloqueado'] = request.POST.get('bloqueado')

        response = requests.put(url, json=usuario_data)

        if response.status_code == 200:
            messages.success(request, "El usuario fue modificado correctamente.")
            return redirect('usuarios')
        else:
            messages.error(request, "No se pudo modificar el usuario.")

    datos = {'usuario_data': usuario_data}
    return render(request, 'mod_usuario.html', datos)