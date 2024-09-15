from django.db import models
from usuarios.models import Usuario

class Consulta(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuesta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descripcion
