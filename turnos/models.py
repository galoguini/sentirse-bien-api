from django.db import models
from usuarios.models import Usuario
from pagos.models import Pago

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    servicio = models.CharField(max_length=100)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos_como_cliente', null=True, blank=True)
    profesional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos_como_profesional', null=True, blank=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fecha} - {self.servicio}'

