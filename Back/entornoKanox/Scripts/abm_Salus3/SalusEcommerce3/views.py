from django.shortcuts import render
#---user
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import RegisterSerializer, UserSerializer
#User
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
#---finUser

# API REST FRAMEWORK CORS
from rest_framework import viewsets
# Tabla UsuariosMedicos
from .models import UsuariosMedicos
from .serializer import UsuarioMedicoSerializer
# Tabla UsuariosPacientes
from .models import UsuariosPacientes
from .serializer import UsuarioPacienteSerializer
# Tabla Sevicios
from .models import Servicios
from .serializer import ServicioSerializer
# Tabla Ventas
from .models import Ventas
from .serializer import VentaSerializer

# Create your views here.
# ------------ API usuario
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= serializer.save()
		return Response({
		"user":UserSerializer(user, context=self.get_serializer_context()).data,
		"token":AuthToken.objects.create(user)[1]
		})

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(LoginAPI, self).post(request,format=None)

# CRUD - ABML
# Tabla UsuariosMedicos
class UsuarioMedicoViewSet(viewsets.ModelViewSet):
 #permission_classes = (permissions.IsAuthenticated,) 

 queryset = UsuariosMedicos.objects.all()
 serializer_class = UsuarioMedicoSerializer

# Tabla UsuariosPacientes
class UsuarioPacienteViewSet(viewsets.ModelViewSet):
 #permission_classes = (permissions.IsAuthenticated,)

 queryset = UsuariosPacientes.objects.all()
 serializer_class = UsuarioPacienteSerializer

# Tabla Sevicios
class ServicioViewSet(viewsets.ModelViewSet):
 #permission_classes = (permissions.IsAdminUser,)

 queryset = Servicios.objects.all()
 serializer_class = ServicioSerializer

# Tabla Ventas
class VentaViewSet(viewsets.ModelViewSet):
 #permission_classes = (permissions.IsAdminUser,)

 queryset = Ventas.objects.all()
 serializer_class = VentaSerializer
