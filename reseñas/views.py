from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Reseña
from .serializers import ReseñaSerializer
from rest_framework.permissions import AllowAny

class ReseñaCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ReseñaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReseñaListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        reseñas = Reseña.objects.all()
        serializer = ReseñaSerializer(reseñas, many=True)
        return Response(serializer.data)
