from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Usuario,Sala,Horario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuario
        fields = ['rut', 'nombre','apellidos', 'correo', 'contraseña','contraseña2','bloqueado']
        labels ={
            'rut': 'rut:', 
            'nombre': 'Nombre:', 
            'apellidos': 'Apellidos:', 
            'correo': 'Correo:', 
            'contraseña': 'Contraseña:', 
            'contraseña2': 'Repetir contraseña:', 
            'bloqueado': 'Bloqueado:',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '99999999k', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellidos', 
                    'id': 'apellidos'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ejemplo@duocuc.cl', 
                    'id': 'correo'
                }
            ), 
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '********', 
                    'id': 'contraseña'
                }
            ), 
            'contraseña2': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '********', 
                    'id': 'contraseña2'
                }
            ), 
            'bloqueado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el stock', 
                    'id': 'bloqueado'
                }
            )

        }
