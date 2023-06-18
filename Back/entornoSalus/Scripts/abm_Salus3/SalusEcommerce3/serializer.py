from rest_framework import serializers

# Tabla UsuariosMedicos
from .models import UsuariosMedicos
# Tabla UsuariosPacientes
from .models import UsuariosPacientes
# Tabla Servicios
from .models import Servicios
# Tabla Ventas
from .models import Ventas

# Tabla UsuariosMedicos
class UsuarioMedicoSerializer(serializers.ModelSerializer):
    class Meta:
       model = UsuariosMedicos
       fields = '__all__'
       #fields = ('id','Nombre_UM','Apellido_UM','Celular_UM','Direccion_UM','Localidad_UM','Dni_UM','Matricula_UM')

# Tabla UsuariosPacientes
class UsuarioPacienteSerializer(serializers.ModelSerializer):
    class Meta:
       model = UsuariosPacientes
       fields = '__all__'
       #fields = ('id','Nombre_UP','Apellido_UP','Email_UP','Clave_UP','Celular_UP','Direccion_UP','Localidad_UP','Dni_UP')

# Tabla Servicios
class ServicioSerializer(serializers.ModelSerializer):
 class Meta:
  model = Servicios
  fields = '__all__'
  #fields = ('id','TipoServicio_S','Precio_S','Descripcion_S')

# Tabla Ventas
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Ventas
       fields = '__all__'
       #fields = ('id','FechaVenta_V','TotalVenta_V','id_UP','id_S')