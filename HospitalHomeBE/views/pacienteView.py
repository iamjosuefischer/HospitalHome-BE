from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.pacienteSerializer import PacienteSerializer
from HospitalHomeBE.models.paciente import Paciente

class PacienteCrearView(views.APIView):
    def post(self, request, format=None):
        serializador=PacienteSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response (serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        modelo=Paciente.objects.all()
        serializar=PacienteSerializer(modelo, many=True)
        return Response (serializar.data)

class Consultar_PacienteView (views.APIView):
    def put (self, request, pk, format=None):
        modelo=Paciente.objects.get(pk=pk)
        serializacion=PacienteSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Paciente.objects.get(pk=pk)
        modelo.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        modelo=Paciente.objects.get(pk=pk)
        serializar= PacienteSerializer(modelo)
        return Response (serializar.data)