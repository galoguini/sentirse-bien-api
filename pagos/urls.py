from django.urls import path
from .views import ProcesarPagoView, PagoListView

urlpatterns = [
    path('procesar/', ProcesarPagoView.as_view()),
    path('lista_pagos/', PagoListView.as_view()),
]
