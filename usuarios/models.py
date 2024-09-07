from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# el username es el CUIL
# rol 0: usuario
# rol 1: staff

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20)
    rol = models.IntegerField()

    def __str__(self):
        return self.email