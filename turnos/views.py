from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Turno
from .serializers import TurnoSerializer

# Vista para elegir (crear) un turno
class ElegirTurno(APIView):
    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para ver los turnos elegidos
class VerTurnos(APIView):
    def get(self, request):
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data)
