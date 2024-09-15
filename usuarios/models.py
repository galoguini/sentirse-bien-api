from django.db import models
from django.contrib.auth.models import AbstractUser

# el username es el email
# rol 0: usuario
# rol 1: staff

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20)
    rol = models.IntegerField()

    def __str__(self):
        return self.email