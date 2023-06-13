from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import Servicios,Cuentas,Ventas,UsuariosMedicos,ServiciosXMedicos,DetallesVentas,UsuariosPacientes,MedicosPacientes,TiposEstudios,HistorialesMedicos,CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import ServicioSerializer
from .serializers import CuentaSerializer
from .serializers import VentaSerializer
from .serializers import UsuarioMedicoSerializer
from .serializers import ServicioXMedicoSerializer
from .serializers import DetalleVentaSerializer
from .serializers import UsuarioPacienteSerializer
from .serializers import MedicoPacienteSerializer
from .serializers import TipoEstudioSerializer
from .serializers import HistorialMedicoSerializer
from rest_framework import viewsets


class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #Solo usuarios logueados pueden ver.
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)

# SERVICIOS ABML
class verServicios(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Servicios.objects.all()
    serializer_class = ServicioSerializer

class agregarServicio(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class modificarServicio(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def put(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarServicio(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def delete(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CUENTAS ABML
class verCuentas(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Cuentas.objects.all()
    serializer_class = CuentaSerializer

class agregarCuenta(APIView):
    permission_classes = [AllowAny] #solo admin
    def post(self, request, format=None):
        serializer = CuentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class modificarCuenta(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def put(self, request, format=None):
        serializer = CuentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarCuenta(APIView):
    permission_classes = [AllowAny] #solo admin
    def delete(self, request, format=None):
        serializer = CuentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# USUARIOSPACIENTES ABML
class verUsuarioPaciente(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = UsuariosPacientes.objects.all()
    serializer_class = UsuarioPacienteSerializer

class agregarUsuarioPaciente(APIView):
    permission_classes = [AllowAny] #solo admin
    def post(self, request, format=None):
        serializer = UsuarioPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class modificarUsuarioPaciente(APIView):
    permission_classes = [AllowAny] #solo admin
    def put(self, request, format=None):
        serializer = UsuarioPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarUsuarioPaciente(APIView):
    permission_classes = [AllowAny] #solo admin
    def delete(self, request, format=None):
        serializer = UsuarioPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
