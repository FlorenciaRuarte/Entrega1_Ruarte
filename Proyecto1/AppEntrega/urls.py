from django.contrib import admin
from django.urls import path
from AppEntrega.views import Especialidades, Medicos, Pacientes, busquedamedico, buscar

urlpatterns = [
    path('especialidades/', Especialidades, name= "especialidades"),
    path('medicos/', Medicos, name= "medicos"),
    path('pacientes/', Pacientes, name= "pacientes"),
    path('busquedamedico/', busquedamedico, name= "busquedamedico"),
    path('buscar/', buscar),

]