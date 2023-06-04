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



class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class verServicios(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny] 
    queryset = Servicios.objects.all()
    serializer_class = ServicioSerializer

class verCuentas(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Cuentas.objects.all()
    serializer_class = CuentaSerializer

class agregarServicio(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)