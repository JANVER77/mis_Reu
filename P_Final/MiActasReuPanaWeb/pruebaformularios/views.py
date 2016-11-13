# pruebaformularios/views.py
from django.views.generic import ListView
from .models import Persona

class PersonaList(ListView):

    model = Persona
