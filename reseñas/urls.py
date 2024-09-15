from django.urls import path
from .views import ReseñaCreateView, ReseñaListView

urlpatterns = [
    path('agregar_reseña/', ReseñaCreateView.as_view()),
    path('mostrar_reseñas/', ReseñaListView.as_view()),
]