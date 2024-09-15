from rest_framework import serializers
from .models import Reseña

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = ['descripcion', 'fecha', 'puntaje', 'nombre']
