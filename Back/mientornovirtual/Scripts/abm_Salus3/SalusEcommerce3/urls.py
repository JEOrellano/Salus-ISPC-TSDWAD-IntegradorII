from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios
from .views import agregarServicios,BMLServicios_Detail
from .views import agregarVentas,BMLVentas_Detail


urlpatterns = [
     # Auth views
     path('auth/login/',
         LoginView.as_view(), name='auth_login'),
     path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
     path('auth/registro/',
         SignupView.as_view(), name='auth_signup'),
     path('user/profile/',
         ProfileView.as_view(), name='user_profile'),
     path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),

     # ABML views
     # Servicios
     path('agregarservicio/',
         agregarServicios.as_view(), name='agregar_servicio'),
     path('servicios/<int:pk>',
         BMLServicios_Detail.as_view(), name='bmlservicios_servicio'),  
    # Ventas
     path('agregarventa/',
         agregarVentas.as_view(), name='agregar_venta'),
     path('ventas/<int:pk>',
         BMLVentas_Detail.as_view(), name='bmlventas_venta'),
]