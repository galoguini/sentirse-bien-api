from rest_framework import generics
from .models import Turno
from .serializers import TurnoSerializer
from rest_framework.permissions import IsAuthenticated

class TurnoListView(generics.ListAPIView):
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        usuario = self.request.user  

        if usuario.rol >= 1:  
            return Turno.objects.all()  
        else:  
            return Turno.objects.filter(usuario=usuario)

class TurnoCreateView(generics.CreateAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
