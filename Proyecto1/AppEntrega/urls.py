from django.contrib import admin
from django.urls import path
from AppEntrega.views import Especialidades, Médicos, Pacientes, busquedamedico, buscar

urlpatterns = [
    path('especialidades/', Especialidades, name= "especialidadesformulario"),
    path('medicosformulario/', Médicos, name= "medicosformulario"),
    path('pacientesformulario/', Pacientes, name= "pacientesformulario"),
    path('busquedamedico/', busquedamedico, name= "busquedamedico"),
    path('buscar/', buscar),

]