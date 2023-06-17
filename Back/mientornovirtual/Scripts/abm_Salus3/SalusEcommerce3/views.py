from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
from .models import Servicios,Ventas,CustomUser
from .serializers import ServicioSerializer,VentaSerializer,UserSerializer

# Create your views here.
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
    permission_classes = [IsAdminUser]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
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

class agregarServicios(APIView):
    permission_classes = [IsAdminUser] #solo admin

    def post(self, request):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BMLServicios_Detail(APIView):
    permission_classes = [IsAdminUser] #solo admin

    '''def get(self,pk):
        servicios = get_object_or_404(Servicios,pk=pk)
        serializer = ServicioSerializer(servicios,many=True)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
    
    # MODIFICAR Servicio por id
    def put(self,request,pk):
        servicios=get_object_or_404(Servicios,pk=pk)
        serializer=ServicioSerializer(servicios,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # BORRAR Servicio por id
    def delete(self,pk):
        servicios=get_object_or_404(Servicios,pk=pk)
        servicios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VENTAS ABML
class verVentas(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Ventas.objects.all()
    serializer_class = VentaSerializer

class agregarVentas(APIView):
    permission_classes = [IsAdminUser] #solo admin

    def post(self, request, format=None):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BMLVentas_Detail(APIView):
    permission_classes = [IsAdminUser] #solo admin

    # VER Venta por id
    '''def get(self,pk):
        ventas = get_object_or_404(Ventas,id_UP=pk)
        serializer = VentaSerializer(ventas)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)'''

    # MODIFICAR Venta por id
    def put(self,request,pk):
        ventas=get_object_or_404(Ventas,pk=pk)
        serializer=VentaSerializer(ventas,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # BORRAR Venta por id
    def delete(self,pk):
        ventas = get_object_or_404(Ventas,pk=pk)
        ventas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    








'''
Reciclado Servicios
class modificarServicios(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def put(self, request, pk, format=None):
        model = get_object_or_404(Servicios,pk=pk)
        serializer = ServicioSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarServicios(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def delete(self, request,pk, format=None):
        model = get_object_or_404(Servicios,pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
class modificarVentas(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def put(self, request, pk, format=None):
        model = get_object_or_404(Ventas,pk=pk)
        serializer = VentaSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class borrarVentas(APIView):
    permission_classes = [IsAdminUser] #solo admin
    def delete(self, request, pk, format=None):
        model = get_object_or_404(Ventas,pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ALVentas(APIView):
    permission_classes = [IsAdminUser] #solo admin    
    # CREAR Venta
    def post(self,request):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
'''