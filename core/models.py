from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut= models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    apellidos= models.CharField(max_length=50, verbose_name='apellido', default='')
    correo= models.EmailField(verbose_name='E-mail')
    contraseña= models.CharField(max_length=50, verbose_name='contraseña',default='sincontraseña')
    contraseña2 = models.CharField(max_length=50, verbose_name='contraseña',default='sincontraseña')
    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Sala(models.Model):
    num= models.IntegerField(primary_key=True, verbose_name='numero de sala')
    descripcion= models.CharField(max_length=50, verbose_name='Descripción')
    disponible= models.BooleanField(default=True)
    def __str__(self):
        return self.descripcion

class Horario(models.Model):
    id= models.CharField(primary_key=True,max_length=4, verbose_name='ID horario')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, verbose_name='Numero de sala')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario:')
    fecha = models.DateField()
    hora_desde = models.TimeField()
    hora_hasta = models.TimeField()

    def __str__(self):
        return self.id