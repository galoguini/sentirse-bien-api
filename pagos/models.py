import random
import string
from django.db import models
from usuarios.models import Usuario

# tipos de pago:
# 0 efectivo/transferencia
# 1 debito
# 2 credito

class Pago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
    turno = models.ForeignKey('turnos.Turno', on_delete=models.CASCADE, null=False, blank=False)
    nroPago = models.CharField(max_length=15, unique=True, editable=False)
    fecha_pago = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if not self.nroPago:
            self.nroPago = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        super().save(*args, **kwargs)

