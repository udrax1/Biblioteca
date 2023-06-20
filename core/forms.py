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
        fields = ['rut', 'nombre', 'correo', 'bloqueado']
        labels ={
            'id': 'Id Producto:', 
            'nombre': 'Nombre:', 
            'correo': 'Correo:', 
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
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ejemplo@duocuc.cl', 
                    'id': 'correo'
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
