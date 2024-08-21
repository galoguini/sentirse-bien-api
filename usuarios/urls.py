from django.urls import path
from rest_framework.authtoken import views
from .views import LogoutView, RegisterView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('registro/', RegisterView.as_view()),
]
