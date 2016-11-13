from django.contrib import admin
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea
#from .views import citaciones, actas, lugares, areas
from App.models import Reuniones, TipoReunion, EstadoReunion, Lugar, temasdos
from .views import FormularioReuniones, tiposreuniones, lugares, estadosreuniones, temasdosp

#Administracion
admin.site.register(Lugar, lugares)
admin.site.register(TipoReunion, tiposreuniones)
admin.site.register(EstadoReunion, estadosreuniones)
#admin.site.register(User, usuario)
#admin.site.register(Acta, actas)
# Register your models here.
admin.site.register(Reuniones, FormularioReuniones)