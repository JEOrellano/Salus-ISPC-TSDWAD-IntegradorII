from django.db import models


# Tabla Servicios
class Servicios(models.Model):
    CodServicio_S=models.CharField(primary_key=True,max_length=6)
    TipoServicio_S=models.CharField(max_length=20, blank=False)
    Precio_S=models.DecimalField(max_digits=18,blank=False,decimal_places=2)
    Descripcion_S=models.CharField(max_length=1000,blank=False)
    class Meta:
        db_table="Servicio"
        verbose_name="Tipo de Servicios"
        verbose_name_plural="Servicios"
    def __unicode__(self):
        return self.CodServicio_S
    def __str__(self):
        return self.CodServicio_S
# Tabla Cuentas
class Cuentas(models.Model):
    CodCuenta_C=models.CharField(primary_key=True,max_length=6)
    Saldo_C=models.DecimalField(max_digits=18,decimal_places=2,blank=True, default=0)
    class Meta:
        db_table="Cuenta"
        verbose_name="Cuentas de usuarios"
        verbose_name_plural="Cuentas"
    def __unicode__(self):
        return self.CodCuenta_C
    def __str__(self):
        return self.CodCuenta_C
# Tabla Ventas
class Ventas(models.Model):
    NroVenta_V=models.AutoField(primary_key=True)
    FechaVenta_V=models.DateField(auto_now_add=True,blank=True)
    TotalVenta_V=models.DecimalField(max_digits=18,decimal_places=2,blank=False)
    CodCuenta_C_V=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="Venta"
        verbose_name="Ventas a Cuentas"
        verbose_name_plural="Ventas"
    def __unicode__(self):
        return self.NroVenta_V
    def __str__(self):
        return self.NroVenta_V
# Tabla UsuariosMedicos
class UsuariosMedicos(models.Model):
    Dni_UM=models.CharField(primary_key=True,max_length=8)
    Matricula_UM=models.CharField(max_length=8,blank=False)
    Nombre_UM=models.CharField(max_length=45,blank=False)
    Apellido_UM=models.CharField(max_length=45,blank=False)
    Celular_UM=models.CharField(max_length=45,blank=False)
    Direccion_UM=models.CharField(max_length=100,blank=False)
    Localidad_UM=models.CharField(max_length=45,blank=False)
    Email_UM=models.CharField(max_length=45,blank=False)
    CodCuenta_UM=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="UsuarioMedico"
        verbose_name="Usuarios Medicos"
        verbose_name_plural="UsuariosMedicos"
    def __unicode__(self):
        return self.Dni_UM
    def __str__(self):
        return self.Dni_UM
# Tabla ServiciosXMedicos
class ServiciosXMedicos(models.Model):
    CodServicio_SXM=models.CharField(primary_key=True,max_length=6)
    Dni_UM_SXM=models.CharField(primary_key=True,max_length=8)
    CodServicio_SXM=models.ForeignKey(Servicios,on_delete=models.CASCADE)
    Dni_UM_SXM=models.ForeignKey(UsuariosMedicos,on_delete=models.CASCADE)
    class Meta:
        db_table="ServicioMedico"
        verbose_name="Servicio y Medico"
        verbose_name_plural="ServiciosMedicos"
    def __unicode__(self):
        return self.CodServicio_SXM
    def __str__(self):
        return self.CodServicio_SXM
# Tabla DetallesVentas
'''class DetallesVentas(models.Model):
    NroVenta_DV=models.IntegerField(primary_key=True)
    CodServicio_SXM_DV=models.CharField(primary_key=True,max_length=6)
    Dni_UM_SXM_DV=models.CharField(primary_key=True,max_length=8)
    PrecioServi_DV=models.DecimalField(max_digits=18,blank=False,decimal_places=2)
    CantServi_DV=models.IntegerField(blank=False)
    NroVenta_DV=models.ForeignKey(Ventas,on_delete=models.CASCADE)
    CodServicio_SXM_DV=models.ForeignKey(ServiciosXMedicos,to_field="CodServicio_SXM",on_delete=models.CASCADE)
    Dni_UM_SXM_DV=models.ForeignKey(ServiciosXMedicos,to_field="Dni_UM_SXM",on_delete=models.CASCADE)
    class Meta:
        db_table="DetalleVenta"
        verbose_name="Detalle y Venta"
        verbose_name_plural="DetallesVentas"
    def __unicode__(self):
        return self.NroVenta_DV
    def __str__(self):
        return self.NroVenta_DV'''
# Tabla UsuariosPacientes
class UsuariosPacientes(models.Model):
    Dni_UP=models.CharField(primary_key=True,max_length=8)
    Nombre_UP=models.CharField(max_length=45,blank=False)
    Apellido_UP=models.CharField(max_length=45,blank=False)
    Celular_UP=models.CharField(max_length=45,blank=False)
    Direccion_UP=models.CharField(max_length=100,blank=False)
    Localidad_UP=models.CharField(max_length=45,blank=False)
    Email_UP=models.CharField(max_length=45,blank=False)
    CodCuenta_UP=models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    class Meta:
        db_table="UsuarioPaciente"
        verbose_name="Usuario Paciente"
        verbose_name_plural="UsuariosPacientes"
    def __unicode__(self):
        return self.Dni_UP
    def __str__(self):
        return self.Dni_UP
# Tabla MedicosPacientes
class MedicosPacientes(models.Model):
    Dni_UM_MP=models.CharField(primary_key=True,max_length=8)
    Dni_UP_MP=models.CharField(primary_key=True,max_length=8)
    Dni_UM_MP=models.ForeignKey(UsuariosMedicos,on_delete=models.CASCADE)
    Dni_UP_MP=models.ForeignKey(UsuariosPacientes,on_delete=models.CASCADE)
    class Meta:
        db_table="MedicoPaciente"
        verbose_name="Medicos Pacientes"
        verbose_name_plural="MedicosPacientes"
    def __unicode__(self):
        return self.Dni_UM_MP
    def __str__(self):
        return self.Dni_UM_MP
# Tabla TiposEstudios
class TiposEstudios(models.Model):
    CodEstudio_TE=models.CharField(primary_key=True,max_length=6)
    NombreEstudio_TE=models.CharField(max_length=45, blank=False)
    Descripcion_TE=models.CharField(max_length=1000,blank=False)
    class Meta:
        db_table="TipoEstudio"
        verbose_name="Tipo de Estudio"
        verbose_name_plural="TiposEstudios"
    def __unicode__(self):
        return self.CodEstudio_TE
    def __str__(self):
        return self.CodEstudio_TE
# Tabla HistorialesMedicos
'''class HistorialesMedicos(models.Model):
    Dni_UM_HM=models.CharField(primary_key=True,max_length=8)
    Dni_UP_HM=models.CharField(primary_key=True,max_length=8)
    CodEstudio_HM=models.CharField(primary_key=True,max_length=6)
    Dni_UM_HM=models.ForeignKey(MedicosPacientes,to_field="Dni_UM_MP",on_delete=models.CASCADE)
    Dni_UP_HM=models.ForeignKey(MedicosPacientes,to_field="Dni_UP_MP",on_delete=models.CASCADE)
    CodEstudio_HM=models.ForeignKey(TiposEstudios,on_delete=models.CASCADE)
    URL_HM=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="HistorialMedico"
        verbose_name="Hisrotial Medico Paciente Tipo Estudio"
        verbose_name_plural="HistorialesMedicos"
    def __unicode__(self):
        return self.Dni_UM_HM
    def __str__(self):
        return self.Dni_UM_HM'''