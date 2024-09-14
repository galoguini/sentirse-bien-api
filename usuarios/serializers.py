from usuarios.models import Usuario  # Cambia la importación
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # Usa el modelo personalizado
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'rol', 'telefono']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)  # Cambia también aquí
        return user
