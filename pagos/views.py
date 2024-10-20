from rest_framework import generics, serializers
from .models import Pago
from .serializers import PagoSerializer
from turnos.models import Turno
from django.utils.dateparse import parse_date

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
    serializer_class = PagoSerializer

    def get_queryset(self):
        queryset = Pago.objects.all()
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')
        if fecha_inicio and fecha_fin:
            fecha_inicio = parse_date(fecha_inicio)
            fecha_fin = parse_date(fecha_fin)
            queryset = queryset.filter(fecha_pago__range=[fecha_inicio, fecha_fin])
        
        return queryset
