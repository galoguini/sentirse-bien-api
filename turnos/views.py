from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Turno
from .serializers import TurnoSerializer
from rest_framework.permissions import AllowAny

class ElegirTurno(APIView):
    permission_classes = [AllowAny] #saca esto dsp!!!!!!!!!!!!!!!!!!
    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerTurnos(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data)
