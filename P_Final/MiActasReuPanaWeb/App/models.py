from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

#User = get_user_model()
# Create your models here.
#Clase para crear la tabla de tipos de reunion.
SINO = (
		('S', 'Disponible'),
		('N', 'No Disponible'),
	)

class TipoReunion(models.Model):
	idTipo = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Tipo Reunion')
		verbose_name_plural = _('Tipos Reuniones')

	def __str__ (self): # __unicode__ on Python 2
		return str(self.descripcion)

#Clase para crear la tabla de Lugares de la reunion.
class Lugar(models.Model):

	idLugar = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50)
	Estado = models.CharField(max_length=1,choices=SINO, null=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Lugar')
		verbose_name_plural = _('Lugares')

	def __str__ (self): # __unicode__ on Python 2
		return str(self.descripcion)

#Clase para crear la tabla de Estado de la reunion.
class EstadoReunion(models.Model):
	idEstado = models.AutoField(primary_key=True)
	NombreEstado = models.CharField(max_length=100)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Estado Reunion')
		verbose_name_plural = _('Estado Reuniones')

	def __str__ (self): # __unicode__ on Python 2
		return str(self.NombreEstado)

#Clase para crear la tabla de Estado de la tarea.
class EstadoTarea(models.Model):
	IdEstadoTarea = models.AutoField(primary_key=True)
	NomEstadoTar = models.CharField(max_length=100, null=True, blank=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

class Reuniones(models.Model):

	CANTIDADHORAS = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)
	IdReunion = models.AutoField(primary_key=True, verbose_name="Numero de Citacion")
	organizador = models.CharField(max_length=50)
	fecha_hora = models.DateTimeField()
	tiempo_estimado = models.IntegerField(null=True, choices=CANTIDADHORAS, help_text='Numero de Horas')
	asunto = models.CharField(max_length=100)
	idTipo = models.ForeignKey(TipoReunion, on_delete=models.CASCADE, null=True)
	idLugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, null=True)
	hora_final = models.TimeField(help_text='HH24:MM:SS')
	idEstado = models.ForeignKey(EstadoReunion,on_delete=models.CASCADE, max_length=2, null=True, blank=True, default='')
	fecha_creacion = models.DateField(auto_now_add=True)
	usuario_creador = models.CharField(max_length=50)
	fecha_modificacion = models.DateField(auto_now=True)
	usuario_modificador = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Reunion')
		verbose_name_plural = _('Reuniones')


	def __str__ (self): # __unicode__ on Python 2
		return str(self.IdReunion)

	def __init__(self, *args, **kwargs):
		super(Reuniones, self).__init__(*args, **kwargs)
		self.__total__ = None


class temasdos(models.Model):
	tema = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100, verbose_name='Nombre Tema')
	Contenido = models.TextField(max_length=4000, null=True, blank=True)
	Acuerdos = models.TextField(max_length=4000, null=True, blank=True)
	idreunion = models.ForeignKey(Reuniones)
	tema_padre_dos = models.ForeignKey('self', null=True, blank=True, verbose_name='Tema a Asociar')

	class Meta:
		verbose_name = _('Tema')
		verbose_name_plural = _('Temas')

	def __str__ (self): # __unicode__ on Python 2
		return str(self.nombre)

class asistentes(models.Model):
	idasis = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, null=True, blank=True, verbose_name='Asistente')
	idReunion = models.ForeignKey(Reuniones, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = _('Asistente')
		verbose_name_plural = _('Asistentes')

	def __str__ (self): # __unicode__ on Python 2
		b = User.objects.get(id=2)
		a = b.first_name + ' ' + b.last_name
		#a = request.user.get_full_name()
		return str(self.user)
