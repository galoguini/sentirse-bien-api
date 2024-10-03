from django.urls import path
from .views import ProcesarPagoView

urlpatterns = [
    path('procesar/', ProcesarPagoView.as_view()),
    # path('nueva_consulta/', ConsultaCreateView.as_view()),
    # path('<int:pk>/respuesta/', ConsultaUpdateView.as_view()),
]