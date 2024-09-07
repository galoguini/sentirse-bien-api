from django.urls import path
from rest_framework.authtoken import views
from .views import LogoutView, RegisterView, GetUserInfoView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('registro/', RegisterView.as_view()),
    path('info_usuario/', GetUserInfoView.as_view()),
]
