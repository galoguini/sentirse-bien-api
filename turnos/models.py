from django.db import models
from usuarios.models import Usuario
from pagos.models import Pago

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.fecha)

    @property
    def pagado(self):
        return Pago.objects.filter(turno=self).exists()
