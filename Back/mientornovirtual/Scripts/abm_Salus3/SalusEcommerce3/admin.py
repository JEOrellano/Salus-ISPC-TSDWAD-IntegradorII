from django.contrib import admin

# Register your models here.
# Tabla Servicios
from .models import Servicios
# Tabla Ventas
from .models import Ventas

# Register your models here.
# Tabla Servicios
class ServicioAdmin(admin.ModelAdmin):
    list_display=("id","TipoServicio_S","Precio_S","Descripcion_S")
# Tabla Ventas
class VentaAdmin(admin.ModelAdmin):
    list_display=("id","FechaVenta_V","TotalVenta_V","id_UP","id_S")

# Registrar tablas
# Tabla Servicios
admin.site.register(Servicios,ServicioAdmin)
# Tabla Ventas
admin.site.register(Ventas,VentaAdmin)

# CUSTOM USER
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

'''@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass'''

admin.site.register(CustomUser)