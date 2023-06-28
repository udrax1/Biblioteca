from django.urls import path
from .views import inicio, login, usuarios, horarios,form_usuarios,eliminar_usuarios,mod_usuarios
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('inicio', inicio,name="inicio"),
    path('usuarios', usuarios,name="usuarios"),
    path('horarios', horarios,name="horarios"),
    path('form_usuarios', form_usuarios,name="form_usuarios"),
    path('eliminar_usuarios/<usuario_id>', eliminar_usuarios,name="eliminar_usuarios"),
    path('mod_usuarios/<id>', mod_usuarios,name="mod_usuarios"),

    ]