from django import forms
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea
#from django.forms import ModelForm
from App.models import Lugar, Reuniones
from django.forms import ModelForm


#Form Citaciones
class RegisReuniones(forms.ModelForm):
	#def __init__(self, *args, **kwargs):
	#	super(RegisCitacion, self).__init__(*args, **kwargs)
	#	self.list_display['citacion_id', 'organizador', 'asunto', 'fecha_hora', 'lugar', 'temas', 'estado'].queryset = Citacione.objects.filter(estado='Activa')

	class Meta:
		model = Reuniones
		fields = ('organizador', 'idTipo', 'idLugar', 'tiempo_estimado', 'asunto')

	def clean_data(self):
		data = self.cleaned_data["asunto"]
		print(data)
