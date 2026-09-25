from django.db import models

# Create your models here.

class ProyectoModels(models.Model):
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    nombre=models.CharField(max_length=20)
    prioridad=models.IntegerField()
    responsable = models.CharField(max_length=100)