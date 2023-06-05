from django.shortcuts import render

# API REST FRAMEWORK CORS
from rest_framework import viewsets
from .serializer import ServicioSerializer
from .serializer import CuentaSerializer
from .serializer import VentaSerializer
from .serializer import UsuarioMedicoSerializer
from .serializer import ServicioXMedicoSerializer
from .serializer import DetalleVentaSerializer
from .serializer import UsuarioPacienteSerializer
from .serializer import MedicoPacienteSerializer
from .serializer import TipoEstudioSerializer
from .serializer import HistorialMedicoSerializer

# Tabla Sevicios
from .models import Servicios
# Tabla Cuentas
from .models import Cuentas
# Tabla Ventas
from .models import Ventas
# Tabla UsuariosMedicos
from .models import UsuariosMedicos
# Tabla ServiciosXMedicos
from .models import ServiciosXMedicos
# Tabla DetallesVentas
from .models import DetallesVentas
# Tabla UsuariosPacientes
from .models import UsuariosPacientes
# Tabla MedicosPacientes
from .models import MedicosPacientes
# Tabla TiposEstudios
from .models import TiposEstudios
# Tabla HistorialesMedicos
from .models import HistorialesMedicos

# Create your views here.

# CRUD - ABML
# Tabla Sevicios
class ServicioViewSet(viewsets.ModelViewSet):
 queryset = Servicios.objects.all()
 serializer_class = ServicioSerializer

# Tabla Cuentas
class CuentaViewSet(viewsets.ModelViewSet):
 queryset = Cuentas.objects.all()
 serializer_class = CuentaSerializer

# Tabla Ventas
class VentaViewSet(viewsets.ModelViewSet):
 queryset = Ventas.objects.all()
 serializer_class = VentaSerializer
# Tabla UsuariosMedicos
class UsuarioMedicoViewSet(viewsets.ModelViewSet):
 queryset = UsuariosMedicos.objects.all()
 serializer_class = UsuarioMedicoSerializer
# Tabla ServiciosXMedicos
class ServicioXMedicoViewSet(viewsets.ModelViewSet):
 queryset = ServiciosXMedicos.objects.all()
 serializer_class = ServicioXMedicoSerializer
# Tabla DetallesVentas
class DetalleVentaViewSet(viewsets.ModelViewSet):
 queryset = DetallesVentas.objects.all()
 serializer_class = DetalleVentaSerializer
# Tabla UsuariosPacientes
class UsuarioPacienteViewSet(viewsets.ModelViewSet):
 queryset = UsuariosPacientes.objects.all()
 serializer_class = UsuarioPacienteSerializer
# Tabla MedicosPacientes
class MedicoPacienteViewSet(viewsets.ModelViewSet):
 queryset = MedicosPacientes.objects.all()
 serializer_class = MedicoPacienteSerializer
# Tabla TiposEstudios
class TipoEstudioViewSet(viewsets.ModelViewSet):
 queryset = TiposEstudios.objects.all()
 serializer_class = TipoEstudioSerializer
# Tabla HistorialesMedicos
class HistorialMedicoViewSet(viewsets.ModelViewSet):
 queryset = HistorialesMedicos.objects.all()
 serializer_class = HistorialMedicoSerializer
