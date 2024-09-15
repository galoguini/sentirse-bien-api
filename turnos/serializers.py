from rest_framework import serializers
from .models import Turno

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['fecha', 'hora', 'servicio', 'usuario']
        read_only_fields = ['usuario']

