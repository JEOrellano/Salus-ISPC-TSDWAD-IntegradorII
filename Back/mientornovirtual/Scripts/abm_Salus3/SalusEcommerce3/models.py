from django.db import models

# Create your models here.
# USER CUSTOM
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)

class ManejadorUsuario(BaseUserManager):
# Crea y guarda a un usuario con el correo y contraseña dadas
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Usuarios deben tener un correo electrónico válido.')    
        usuario=self.model(
            email=self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
# Crea y guarda un usuario staff
    def create_staffuser(self,email,password):
        usuario=self.create_user(
            email,
            password=password
        )
        usuario.staff=True
        usuario.save(using=self._db)
        return usuario
# Crea y guarda a un super-usuario
    def create_superuser(self,email,password):
        usuario=self.create_user(
            email,
            password=password
        )
        usuario.staff=True
        usuario.admin=True
        usuario.save(using=self._db)
        return usuario
    
class CustomUser(AbstractBaseUser):
    Nombre_UP=models.CharField(max_length=45,blank=True,default="Nombre_UP")
    Apellido_UP=models.CharField(max_length=45,blank=True,default="Apellido_UP")
    email = models.EmailField(verbose_name='correo electronico',max_length=150, unique=True)
    Celular_UP=models.CharField(max_length=45,blank=True,default="Celular_UP")
    Direccion_UP=models.CharField(max_length=100,blank=True,default="Direccion_UP")
    Localidad_UP=models.CharField(max_length=45,blank=True,default="Localidad_UP")
    Dni_UP=models.CharField(max_length=8,blank=True,default="Dni_UP")

    active = models.BooleanField('Activo', default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    # Establecer el manejador de modelo (definido en el siguiente paso)
    objects = ManejadorUsuario()
    USERNAME_FIELD = 'email' # definimos el correo como el "nombre de usuario"
    REQUIRED_FIELDS = [] # email y password requeridos por defecto
    class Meta: # cambiar cómo aparece nombrado el modelo en la seccion de administracion de Django
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
    def get_full_name(self):
        return self.Nombre_UP+' '+self.Apellido_UP    
    def get_short_name(self):
        return self.Nombre_UP    
    def has_perm(self,perm,obj=None):
        "¿El usuario cuenta con un permiso en especifico?"
        return True    
    def has_module_perms(self, app_label):
        "¿El usuario cuenta con los permisos para ver una app en especifico?"
        # Lo más simple, si
        return True    
    @property
    def is_staff(self):
        "¿El usuario es staff (no super-usuario)?"
        return self.staff    
    @property
    def is_admin(self):
        "¿El usuario es un administrador (super-usuario)?"
        return self.admin    
    @property
    def is_active(self):
        "¿El usuario está activo?"
        return self.active    
    def __str__(self):
        return self.Nombre_UP+' '+self.Apellido_UP+' '+self.email
    
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
    
# Tabla Ventas
class Ventas(models.Model):
    FechaVenta_V=models.DateField(auto_now_add=True,blank=True)
    TotalVenta_V=models.DecimalField(max_digits=18,decimal_places=2,blank=False)
    id_UP=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,default=1)
    id_S=models.ForeignKey(Servicios,on_delete=models.CASCADE,blank=True,default=1)
    class Meta:
        db_table="Ventas"
        verbose_name="Ventas a Cuentas"
        verbose_name_plural="Ventas"
    def __unicode__(self):
        return "{}".format(self.id)
    def __str__(self):
        return "{}".format(self.id)
    
