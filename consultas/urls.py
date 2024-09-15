from django.urls import path
from .views import ConsultaCreateView, ConsultaUpdateView, ConsultaListView

urlpatterns = [
    path('mostrar_consultas/', ConsultaListView.as_view()),
    path('nueva_consulta/', ConsultaCreateView.as_view()),
    path('<int:pk>/respuesta/', ConsultaUpdateView.as_view()),
]