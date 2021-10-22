from django.db import models

# Create your models here.

class personas (models.model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    genero = models.CharField(max_length=50)

