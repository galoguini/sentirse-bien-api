# Create your views here.

from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import RegisterSerializer, UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Usuario
from rest_framework.exceptions import PermissionDenied

class CambiarRolUsuarioView(APIView):
    def patch(self, request, pk):
        try:
            rol = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioSerializer(rol, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosListView(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        usuario = self.request.user

        if usuario.rol >= 1:
            return Usuario.objects.all()
        else:
            raise PermissionDenied({"error": "Acceso denegado, solo para roles de administración"})

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetUserInfoView(APIView):
    serializer_class = UsuarioSerializer

    def get(self, request):
        usuario = self.request.user
        serializer = self.serializer_class(usuario)

        return Response(serializer.data, status=status.HTTP_200_OK)
