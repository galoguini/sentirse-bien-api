from django.urls import path
from .views import ProcesarPagoView, PagoListView

urlpatterns = [
    path('procesar/', ProcesarPagoView.as_view()),
    path('pagos/', PagoListView.as_view()),
]
