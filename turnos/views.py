from rest_framework import generics
from .models import Turno
from .serializers import TurnoSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Usuario
import random

class TurnoListView(generics.ListAPIView):
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        usuario = self.request.user  
        if usuario.rol >= 1:  
            return Turno.objects.all()  
        else:  
            return Turno.objects.filter(cliente=usuario)

class TurnoCreateView(generics.CreateAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profesionales = Usuario.objects.filter(rol=1)
        profesional_random = random.choice(profesionales) if profesionales.exists() else None
        serializer.save(cliente=self.request.user, profesional=profesional_random)
