from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios, agregarServicio

urlpatterns = [
     path('agregarservicio/',
         agregarServicio.as_view(), name='agregar_servicio'),
]