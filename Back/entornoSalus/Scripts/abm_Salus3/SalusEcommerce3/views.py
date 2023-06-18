from django.shortcuts import render
#--- mercadopago
import mercadopago
import json
from rest_framework.views import APIView
from rest_framework.response import Response

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

# CRUD - ABML
# Tabla UsuariosMedicos
class UsuarioMedicoViewSet(viewsets.ModelViewSet):
 
 queryset = UsuariosMedicos.objects.all()
 serializer_class = UsuarioMedicoSerializer

# Tabla UsuariosPacientes
class UsuarioPacienteViewSet(viewsets.ModelViewSet):
 queryset = UsuariosPacientes.objects.all()
 serializer_class = UsuarioPacienteSerializer

# Tabla Sevicios
class ServicioViewSet(viewsets.ModelViewSet):
 queryset = Servicios.objects.all()
 serializer_class = ServicioSerializer

# Tabla Ventas
class VentaViewSet(viewsets.ModelViewSet):
 queryset = Ventas.objects.all()
 serializer_class = VentaSerializer

# pasarela de pago mercadolibre
class ProcessPaymentAPIView(APIView):
    def post(self, request):
        try:
            request_values = json.loads(request.body)
            payment_data = {
                "transaction_amount": float(request_values["transaction_amount"]),
                "token": request_values["token"],
                "installments": int(request_values["installments"]),
                "payment_method_id": request_values["payment_method_id"],
                "issuer_id": request_values["issuer_id"],
                "payer": {
                    "email": request_values["payer"]["email"],
                    "identification": {
                        "type": request_values["payer"]["identification"]["type"],
                        "number": request_values["payer"]["identification"]["number"],
                    },
                },
            }

            sdk = mercadopago.SDK("")

            payment_response = sdk.payment().create(payment_data)

            payment = payment_response["response"]
            status = {
                "id": payment["id"],
                "status": payment["status"],
                "status_detail": payment["status_detail"],
            }

            return Response(data={"body": status, "statusCode": payment_response["status"]}, status=201)
        except Exception as e:
            return Response(data={"body": payment_response}, status=400)

class retornarPagado(APIView):  # Retornar custom json 
    def get(self, request):
        return Response({"respuesta": "aprobado"})