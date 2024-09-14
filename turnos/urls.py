from django.urls import path
from .views import ElegirTurno, VerTurnos

urlpatterns = [
    path('elegir_turno/', ElegirTurno.as_view()),
    path('obtener_turnos/', VerTurnos.as_view()),
]
