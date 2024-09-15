from django.urls import path
from .views import TurnoCreateView, TurnoListView

urlpatterns = [
    path('elegir_turno/', TurnoCreateView.as_view()),
    path('obtener_turnos/', TurnoListView.as_view()),
]
