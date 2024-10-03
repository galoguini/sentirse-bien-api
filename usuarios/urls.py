from django.urls import path
from rest_framework.authtoken import views
from .views import LogoutView, RegisterView, GetUserInfoView, UsuariosListView, CambiarRolUsuarioView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('registro/', RegisterView.as_view()),
    path('info_usuario/', GetUserInfoView.as_view()),
    path('listar_usuarios/', UsuariosListView.as_view()),
    path('<int:pk>/rol/', CambiarRolUsuarioView.as_view()),
]
