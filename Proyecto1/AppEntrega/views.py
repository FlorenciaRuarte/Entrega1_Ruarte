from asyncio.base_subprocess import ReadSubprocessPipeProto
from django.http import HttpResponse
from django.shortcuts import render

from AppEntrega.forms import pacientesformulario, medicosformulario, especialidadesformulario
from AppEntrega.models import Paciente, Medico

# Create your views here.

def Especialidades (request):
    if request.method == 'POST':
        espFormulario = especialidadesformulario(request.POST)
        print(espFormulario)
        if espFormulario.is_valid:
            
            informacion = espFormulario.data
            
            r_nombre = informacion['nombre']

        
            especialidad = Especialidades(nombre=r_nombre)
            especialidad.save()
    
    espFormulario = especialidadesformulario()
    return render(request, 'AppEntrega/especialidadesformulario.html', {"espFormulario": espFormulario})

def Médicos (request):
    if request.method == 'POST':
        medFormulario = medicosformulario(request.POST)
        print(medFormulario)
        if medFormulario.is_valid:
            
            informacion = medFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_email = informacion['email']
        
            medico = Medico(nombre=r_nombre, apellido=r_apellido, email= r_email)
            medico.save()
    
    medFormulario = medicosformulario()
    return render(request, 'AppEntrega/medicosformulario.html', {"medFormulario": medFormulario})




def Pacientes(request):
    if request.method == 'POST':
        miFormulario = pacientesformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_email = informacion['email']
        
            paciente = Paciente(nombre=r_nombre, apellido=r_apellido, email= r_email)
            paciente.save()
    
    miFormulario = pacientesformulario()
    return render(request, 'AppEntrega/pacientesformulario.html', {"miFormulario": miFormulario})
    
def busquedamedico(request):
    return render(request, "AppEntrega/busquedamedico.html")

def buscar(request):
    if request.GET["medico"]:
        resultadomedico = request.GET['medico']
        medicos = Medico.objects.filter(apellido__icontains=resultadomedico)
        return render(request, "AppEntrega/busquedamedico.html", {"medico": medicos} )

    else:
        error= "No enviaste datos"

    return render(request, "AppEntrega/busquedamedico.html", {"error": error} )