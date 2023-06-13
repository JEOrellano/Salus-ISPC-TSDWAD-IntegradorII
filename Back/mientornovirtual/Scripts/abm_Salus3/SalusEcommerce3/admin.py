from django.contrib import admin

# Register your models here.
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

# Register your models here.
# Tabla Servicios
class ServicioAdmin(admin.ModelAdmin):
    list_display=("id","TipoServicio_S","Precio_S","Descripcion_S")
# Tabla Cuentas
class CuentaAdmin(admin.ModelAdmin):
    list_display=("id","Saldo_C")
# Tabla Ventas
class VentaAdmin(admin.ModelAdmin):
    list_display=("id","FechaVenta_V","TotalVenta_V","id_C")
# Tabla UsuariosMedicos
class UsuarioMedicoAdmin(admin.ModelAdmin):
    list_display=("id","Nombre_UM","Apellido_UM","Email_UM","Clave_UM","Celular_UM","Direccion_UM","Localidad_UM","Dni_UM","Matricula_UM","id_C")
# Tabla ServiciosXMedicos
class ServicioXMedicoAdmin(admin.ModelAdmin):
    list_display=("id","id_S","id_UM")
# Tabla DetallesVentas
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display=("id","PrecioServi_DV","CantServi_DV","id_V","id_SXM")
# Tabla UsuariosPacientes
class UsuarioPacienteAdmin(admin.ModelAdmin):
    list_display=("id","Nombre_UP","Apellido_UP","Email_UP","Clave_UP","Celular_UP","Direccion_UP","Localidad_UP","Dni_UP","id_C")
# Tabla MedicosPacientes
class MedicoPacienteAdmin(admin.ModelAdmin):
    list_display=("id","id_UM","id_UP")
# Tabla TiposEstudios
class TipoEstudioAdmin(admin.ModelAdmin):
    list_display=("id","NombreEstudio_TE","Descripcion_TE")
# Tabla HistorialesMedicos
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display=("id","URL_HM","id_MP","id_TE")

# Registrar tablas
# Tabla Servicios
admin.site.register(Servicios,ServicioAdmin)
# Tabla Cuentas
admin.site.register(Cuentas,CuentaAdmin)
# Tabla Ventas
admin.site.register(Ventas,VentaAdmin)
# Tabla UsuariosMedicos
admin.site.register(UsuariosMedicos,UsuarioMedicoAdmin)
# Tabla ServiciosXMedicos
admin.site.register(ServiciosXMedicos,ServicioXMedicoAdmin)
# Tabla DetallesVentas
admin.site.register(DetallesVentas,DetalleVentaAdmin)
# Tabla UsuariosPacientes
admin.site.register(UsuariosPacientes,UsuarioPacienteAdmin)
# Tabla MedicosPacientes
admin.site.register(MedicosPacientes,MedicoPacienteAdmin)
# Tabla TiposEstudios
admin.site.register(TiposEstudios,TipoEstudioAdmin)
# Tabla HistorialesMedicos
admin.site.register(HistorialesMedicos,HistorialMedicoAdmin)

# CUSTOM USER
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models  import CustomUser


# Register your models here.

'''@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass'''

admin.site.register(CustomUser)