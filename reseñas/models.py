from django.db import models

class Reseña(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    puntaje = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.puntaje