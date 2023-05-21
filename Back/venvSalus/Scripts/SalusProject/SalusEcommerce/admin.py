from django.contrib import admin

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
'''from .models import DetallesVentas'''
# Tabla UsuariosPacientes
from .models import UsuariosPacientes
# Tabla MedicosPacientes
from .models import MedicosPacientes
# Tabla TiposEstudios
from .models import TiposEstudios
# Tabla HistorialesMedicos
'''from .models import HistorialesMedicos'''

# Register your models here.
# Tabla Servicios
class ServicioAdmin(admin.ModelAdmin):
    list_display=("CodServicio_S","TipoServicio_S","Precio_S","Descripcion_S")
# Tabla Cuentas
class CuentaAdmin(admin.ModelAdmin):
    list_display=("CodCuenta_C","Saldo_C")
# Tabla Ventas
class VentaAdmin(admin.ModelAdmin):
    list_display=("NroVenta_V","FechaVenta_V","TotalVenta_V","CodCuenta_C_V")
# Tabla UsuariosMedicos
class UsuarioMedicoAdmin(admin.ModelAdmin):
    list_display=("Dni_UM","Matricula_UM","Nombre_UM","Apellido_UM","Celular_UM","Direccion_UM","Localidad_UM","Email_UM","CodCuenta_UM")
# Tabla ServiciosXMedicos
class ServicioXMedicoAdmin(admin.ModelAdmin):
    list_display=("CodServicio_SXM","Dni_UM_SXM")
# Tabla DetallesVentas
'''class DetalleVentaAdmin(admin.ModelAdmin):
    list_display=("NroVenta_DV","CodServicio_SXM_DV","Dni_UM_SXM_DV","PrecioServi_DV","CantServi_DV")'''
# Tabla UsuariosPacientes
class UsuarioPacienteAdmin(admin.ModelAdmin):
    list_display=("Dni_UP","Nombre_UP","Apellido_UP","Celular_UP","Direccion_UP","Localidad_UP","Email_UP","CodCuenta_UP")
# Tabla MedicosPacientes
class MedicoPacienteAdmin(admin.ModelAdmin):
    list_display=("Dni_UM_MP","Dni_UP_MP")
# Tabla TiposEstudios
class TipoEstudioAdmin(admin.ModelAdmin):
    list_display=("CodEstudio_TE","NombreEstudio_TE","Descripcion_TE")
# Tabla HistorialesMedicos
'''class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display=("Dni_UM_HM","Dni_UP_HM","CodEstudio_HM","URL_HM")'''

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
'''admin.site.register(DetallesVentas,DetalleVentaAdmin)'''
# Tabla UsuariosPacientes
admin.site.register(UsuariosPacientes,UsuarioPacienteAdmin)
# Tabla MedicosPacientes
admin.site.register(MedicosPacientes,MedicoPacienteAdmin)
# Tabla TiposEstudios
admin.site.register(TiposEstudios,TipoEstudioAdmin)
# Tabla HistorialesMedicos
'''admin.site.register(HistorialesMedicos,HistorialMedicoAdmin)'''
