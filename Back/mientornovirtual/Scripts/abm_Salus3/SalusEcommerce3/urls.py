from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios
from .views import agregarServicio,modificarServicio,borrarServicio
from .views import agregarCuenta, modificarCuenta, borrarCuenta
from .views import agregarUsuarioPaciente, modificarUsuarioPaciente, borrarUsuarioPaciente

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
    path('agregarservicio/',
         agregarServicio.as_view(), name='agregar_servicio'),
         
    path('modificarservicio/',
         modificarServicio.as_view(), name='modificar_servicio'),

    path('borrarservicio/',
         borrarServicio.as_view(), name='borrar_servicio'),

    path('agregarcuenta/',
         agregarCuenta.as_view(), name='agregar_cuenta'),

    path('modificarcuenta/',
         modificarCuenta.as_view(), name='modificar_cuenta'),
    
    path('borrarcuenta/',
         borrarCuenta.as_view(), name='borrar_cuenta'),

    path('agregarusuariopaciente/',
         agregarUsuarioPaciente.as_view(), name='agregar_usuariopaciente'),

    path('modificarusuariopaciente/',
         modificarUsuarioPaciente.as_view(), name='modificar_usuariopaciente'),
    
    path('borrarusuariopaciente/',
         borrarUsuarioPaciente.as_view(), name='borrar_usuariopaciente'),
]