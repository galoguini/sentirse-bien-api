from django.db import models
from usuarios.models import Usuario

class Reseña(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    puntaje = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nombre_no_registrado = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.puntaje