from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fecha
