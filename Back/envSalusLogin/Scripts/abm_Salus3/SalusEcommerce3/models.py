from django.db import models

# Create your models here.
# Tabla Servicios
class Servicios(models.Model):
    TipoServicio_S=models.CharField(max_length=20)
    Precio_S=models.DecimalField(max_digits=18,decimal_places=2)
    Descripcion_S=models.CharField(max_length=1000)
    class Meta:
        db_table="Servicios"
        verbose_name="Tipo de Servicios"
        verbose_name_plural="Servicios"
    def __unicode__(self):
        return self.TipoServicio_S
    def __str__(self):
        return self.TipoServicio_S
# Tabla Cuentas
class Cuentas(models.Model):
    Saldo_C=models.DecimalField(max_digits=18,decimal_places=2,blank=True, default=0)
    class Meta:
        db_table="Cuentas"
        verbose_name="Cuentas de usuarios"
        verbose_name_plural="Cuentas"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla Ventas
class Ventas(models.Model):
    FechaVenta_V=models.DateField(auto_now_add=True,blank=True)
    TotalVenta_V=models.DecimalField(max_digits=18,decimal_places=2,blank=False)
    id_C=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="Ventas"
        verbose_name="Ventas a Cuentas"
        verbose_name_plural="Ventas"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla UsuariosMedicos
class UsuariosMedicos(models.Model):
    Nombre_UM=models.CharField(max_length=45)
    Apellido_UM=models.CharField(max_length=45)
    Email_UM=models.CharField(max_length=45)
    Clave_UM=models.CharField(max_length=45)
    Celular_UM=models.CharField(max_length=45,blank=True,default="Celular_UM")
    Direccion_UM=models.CharField(max_length=100,blank=True,default="Direccion_UM")
    Localidad_UM=models.CharField(max_length=45,blank=True,default="Localidad_UM")
    Dni_UM=models.CharField(max_length=8,blank=True,default="Dni_UM")
    Matricula_UM=models.CharField(max_length=8,blank=True,default="Mat_UM")
    id_C=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="UsuariosMedicos"
        verbose_name="Usuarios Medicos"
        verbose_name_plural="UsuariosMedicos"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla ServiciosXMedicos
class ServiciosXMedicos(models.Model):
    id_S=models.ForeignKey(Servicios,on_delete=models.CASCADE)
    id_UM=models.ForeignKey(UsuariosMedicos,on_delete=models.CASCADE)
    class Meta:
        db_table="ServiciosXMedicos"
        verbose_name="Servicio y Medico"
        verbose_name_plural="ServiciosMedicos"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla DetallesVentas
class DetallesVentas(models.Model):
    PrecioServi_DV=models.DecimalField(max_digits=18,decimal_places=2)
    CantServi_DV=models.IntegerField()
    id_V=models.ForeignKey(Ventas,on_delete=models.CASCADE)
    id_SXM=models.ForeignKey(ServiciosXMedicos,on_delete=models.CASCADE)
    class Meta:
        db_table="DetallesVentas"
        verbose_name="Detalle y Venta"
        verbose_name_plural="DetallesVentas"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla UsuariosPacientes
class UsuariosPacientes(models.Model):
    Nombre_UP=models.CharField(max_length=45)
    Apellido_UP=models.CharField(max_length=45)
    Email_UP=models.CharField(max_length=45)
    Clave_UP=models.CharField(max_length=45)
    Celular_UP=models.CharField(max_length=45,blank=True,default="Celular_UP")
    Direccion_UP=models.CharField(max_length=100,blank=True,default="Direccion_UP")
    Localidad_UP=models.CharField(max_length=45,blank=True,default="Localidad_UP")
    Dni_UP=models.CharField(max_length=8,blank=True,default="Dni_UP")
    id_C=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="UsuariosPacientes"
        verbose_name="Usuarios Pacientes"
        verbose_name_plural="UsuariosPacientes"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla MedicosPacientes
class MedicosPacientes(models.Model):
    id_UM=models.ForeignKey(UsuariosMedicos,on_delete=models.CASCADE)
    id_UP=models.ForeignKey(UsuariosPacientes,on_delete=models.CASCADE)
    class Meta:
        db_table="MedicosPacientes"
        verbose_name="Medicos Pacientes"
        verbose_name_plural="MedicosPacientes"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla TiposEstudios
class TiposEstudios(models.Model):
    NombreEstudio_TE=models.CharField(max_length=45)
    Descripcion_TE=models.CharField(max_length=1000)
    class Meta:
        db_table="TiposEstudios"
        verbose_name="Tipo de Estudio"
        verbose_name_plural="TiposEstudios"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
# Tabla HistorialesMedicos
class HistorialesMedicos(models.Model):
    URL_HM=models.CharField(max_length=100)
    id_MP=models.ForeignKey(MedicosPacientes,on_delete=models.CASCADE)
    id_TE=models.ForeignKey(TiposEstudios,on_delete=models.CASCADE)
    class Meta:
        db_table="HistorialesMedicos"
        verbose_name="Hisrotial Medico Paciente Tipo Estudio"
        verbose_name_plural="HistorialesMedicos"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)

# USER CUSTOM
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']