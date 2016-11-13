# pruebaformularios/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'list/$', views.PersonaList.as_view(), name='plist'),

]
