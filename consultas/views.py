from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Consulta
from .serializers import ConsultaSerializer
from rest_framework.permissions import AllowAny

class ConsultaListView(APIView):
    def get(self, request):
        usuario = request.user 

        if usuario.rol == 1: 
            consultas = Consulta.objects.all() 
        else: 
            consultas = Consulta.objects.filter(usuario=usuario)

        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConsultaUpdateView(APIView):
    def patch(self, request, pk):
        try:
            consulta = Consulta.objects.get(pk=pk)
        except Consulta.DoesNotExist:
            return Response({"error": "Consulta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ConsultaSerializer(consulta, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultaCreateView(APIView):

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()
        data['usuario'] = request.user.id
        serializer = ConsultaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

