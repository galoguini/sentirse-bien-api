from rest_framework import generics, serializers
from .models import Pago
from .serializers import PagoSerializer
from turnos.models import Turno

class ProcesarPagoView(generics.CreateAPIView):
    serializer_class = PagoSerializer

    def perform_create(self, serializer):
        turno_id = self.request.data.get('turno')
        monto = self.request.data.get('monto')

        try:
            turno = Turno.objects.get(id=turno_id)
            serializer.save(usuario=self.request.user, turno=turno, monto=monto)
        except Turno.DoesNotExist:
            raise serializers.ValidationError("Turno no encontrado")

class PagoListView(generics.ListAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
