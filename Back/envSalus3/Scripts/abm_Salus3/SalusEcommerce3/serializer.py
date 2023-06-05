from rest_framework import serializers

# Tabla Servicios
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

# Tabla Servicios
class ServicioSerializer(serializers.ModelSerializer):
 class Meta:
  model = Servicios
  fields = '__all__'
  #fields = ('id','TipoServicio_S','Precio_S','Descripcion_S')

# Tabla Cuentas
class CuentaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cuentas
    fields = '__all__'
    #fields=('id','Saldo_C')

# Tabla Ventas
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Ventas
       fields = '__all__'
       #fields = ('id','FechaVenta_V','TotalVenta_V','id_C')
# Tabla UsuariosMedicos
class UsuarioMedicoSerializer(serializers.ModelSerializer):
    class Meta:
       model = UsuariosMedicos
       fields = '__all__'
       #fields = ('id','Nombre_UM','Apellido_UM','Email_UM','Clave_UM','Celular_UM','Direccion_UM','Localidad_UM','Dni_UM','Matricula_UM','id_C')
# Tabla ServiciosXMedicos
class ServicioXMedicoSerializer(serializers.ModelSerializer):
    class Meta:
       model = ServiciosXMedicos
       fields = '__all__'
       #fields = ('id','id_S','id_UM')
# Tabla DetallesVentas
class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
       model = DetallesVentas
       fields = '__all__'
       #fields = ('id','PrecioServi_DV','CantServi_DV','id_V','id_SXM')
# Tabla UsuariosPacientes
class UsuarioPacienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = UsuariosPacientes
       fields = '__all__'
       #fields = ('id','Nombre_UP','Apellido_UP','Email_UP','Clave_UP','Celular_UP','Direccion_UP','Localidad_UP','Dni_UP','id_C')
# Tabla MedicosPacientes
class MedicoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = MedicosPacientes
       fields = '__all__'
       #fields = ('id','id_UM','id_UP')
# Tabla TiposEstudios
class TipoEstudioSerializer(serializers.ModelSerializer):
    class Meta:
       model = TiposEstudios
       fields = '__all__'
       #fields = ('id','NombreEstudio_TE','Descripcion_TE')
# Tabla HistorialesMedicos
class HistorialMedicoSerializer(serializers.ModelSerializer):
    class Meta:
       model = HistorialesMedicos
       fields = '__all__'
       #fields = ('id','URL_HM','id_MP','id_TE')