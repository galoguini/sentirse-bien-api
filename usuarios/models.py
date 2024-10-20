from django.db import models
from django.contrib.auth.models import AbstractUser

# el username es el email
# rol 0: usuario
# rol 1: staff
# rol 2: secretaria
# rol 3: administrador (no es admin django)

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20)
    rol = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.email