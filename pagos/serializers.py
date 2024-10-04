from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['usuario', 'turno', 'monto', 'nroPago']
        read_only_fields = ['usuario', 'nroPago'] 
