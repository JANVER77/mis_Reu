from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#
from django import forms
from django.contrib import admin
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea, PuenteActaTema
#from .forms import RegisCitacion, RegisActa
from django.forms.models import BaseInlineFormSet
#from django.forms import BaseFormSet
from django.forms import formset_factory
from django.core.mail import send_mail
from django_admin_bootstrapped.admin.models import SortableInline
from django_admin_bootstrapped.widgets import GenericContentTypeSelect
from django.forms.widgets import CheckboxSelectMultiple
from App.models import Lugar, Reuniones, TipoReunion, EstadoReunion, EstadoTarea, temasdos, asistentes
from .forms import RegisReuniones
# Create your views here.
from django.contrib.auth.models import User



#class tareas(admin.TabularInline):
#	model = Tarea
#	fields = ('descripcion', 'responsable', 'fecha_limite', 'observaciones', 'cumplido')
#	extra = 0

#class Tema(admin.TabularInline):
#	model = Tema.tema_id.through
#	#fields = ('reu_id',)
#	#inlines = (tareas)
#	extra = 0


#class FormularioReuniones(admin.ModelAdmin):
#	form = RegisReuniones #Generar un orden de visualizacion
#	inlines = (Temas, ) #Bloques detalle otros asistentes y compromisos

class lugares(admin.ModelAdmin):
	fields = ('descripcion', )


class tiposreuniones(admin.ModelAdmin):
	fields = ('descripcion', )

class estadosreuniones(admin.ModelAdmin):
	fields = ('NombreEstado', )

#class temasdosp(admin.TabularInline):
class temasdosp(admin.StackedInline, SortableInline):
    model = temasdos
    fields = ('nombre', 'Contenido', 'Acuerdos', 'tema_padre_dos')
    extra = 0



class asistentesreunion(admin.TabularInline):
    model = asistentes
    #user = request.user.get_full_name()
    fields = ('user', )
    extra = 0

class FormularioReuniones(admin.ModelAdmin):
    form = RegisReuniones
    inlines = [
        temasdosp, asistentesreunion,
    ]
    #exclude = ('idTema',)
    fieldsets = (
        ('Agendamiento y Registro de Reunion', {
            'fields': ['organizador', 'fecha_hora', 'idTipo', 'idLugar', 'tiempo_estimado', 'hora_final', 'asunto', 'idEstado'] #'citacion',
        }),
        #('Temas, Contenido, Acuerdos', {
        #    'classes': ('collapse',),
        #    'fields': ('temas', 'contenido', 'acuerdos',),
        #}),
    )
    list_display = ['organizador', 'fecha_hora', 'idTipo', 'idLugar', 'tiempo_estimado', 'hora_final', 'asunto']
    search_fields = ['organizador', 'fecha_hora', 'tiempo_estimado', 'hora_final', 'asunto']
    list_filter = ['organizador', 'fecha_hora', 'idTipo', 'idLugar', ]
	#raw_id_fields = ['citacion_id'] #Buscar por el numero de acta
