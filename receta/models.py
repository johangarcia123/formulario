from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion         = models.CharField(max_length=50)
    fecha       = models.CharField(max_length=50)
