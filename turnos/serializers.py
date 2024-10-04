from rest_framework import serializers
from .models import Turno

class TurnoSerializer(serializers.ModelSerializer):
    pagado = serializers.BooleanField(read_only=True)

    class Meta:
        model = Turno
        fields = ['fecha', 'hora', 'servicio', 'usuario', 'pagado'] 
