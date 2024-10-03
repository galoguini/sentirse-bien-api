from django.db import models
from usuarios.models import Usuario
from turnos.models import Turno

# Create your models here.

class Pago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)
    monto = models.IntegerField(null=False, blank=False)