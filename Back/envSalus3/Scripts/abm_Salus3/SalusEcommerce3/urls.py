from django.urls import path, include
from rest_framework import routers

# from Servicios.views import ServicioViewSet
from SalusEcommerce3  import views

router= routers.DefaultRouter()
router.register(r'servicios',views.ServicioViewSet)
router.register(r'cuentas',views.CuentaViewSet)
router.register(r'ventas',views.VentaViewSet)
router.register(r'usuariosmedicos',views.UsuarioMedicoViewSet)
router.register(r'serviciosxmedicos',views.ServicioXMedicoViewSet)
router.register(r'detallesventas',views.DetalleVentaViewSet)
router.register(r'usuariospacientes',views.UsuarioPacienteViewSet)
router.register(r'medicospacientes',views.MedicoPacienteViewSet)
router.register(r'tiposestudios',views.TipoEstudioViewSet)
router.register(r'historialesmedicos',views.HistorialMedicoViewSet)
#----
urlpatterns = [
    path('', include(router.urls)),
]