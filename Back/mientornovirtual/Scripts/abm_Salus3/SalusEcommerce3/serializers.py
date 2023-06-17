from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Servicios,Ventas
from django.contrib.auth.hashers import make_password

# USER CUSTOM
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','Nombre_UP','Apellido_UP','email','password','Celular_UP','Direccion_UP','Localidad_UP','Dni_UP','admin')
    def validate_password(self, value):
        return make_password(value)

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
       #fields = ('id','FechaVenta_V','TotalVenta_V','id_UP','id')