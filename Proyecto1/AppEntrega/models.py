from django.db import models

# Create your models here.

class Especialidades (models.Model):
    nombre= models.CharField(max_length=40)
    
   
class Medico (models.Model):
    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Paciente (models.Model):
    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
