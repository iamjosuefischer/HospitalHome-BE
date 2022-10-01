from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.enfermeroSerializer import EnfermeroSerializer
from HospitalHomeBE.serializers.usuarioSerializer import UsuarioSerializer
from HospitalHomeBE.models.enfermero import Enfermero

class EnfermeroCrearView(views.APIView):
    def post(self, request, format=None):
        serializador=EnfermeroSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response (serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        modelo=Enfermero.objects.all()
        serializar=EnfermeroSerializer(modelo, many=True)
        return Response (serializar.data)

class ConsultarEnfermeroView (views.APIView):
    def put (self, request, pk, format=None):
        modelo=Enfermero.objects.get(pk=pk)
        serializacion=EnfermeroSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Enfermero.objects.get(pk=pk)
        modelo.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        modelo=Enfermero.objects.get(pk=pk)
        serializar= EnfermeroSerializer(modelo)
        return Response (serializar.data)

