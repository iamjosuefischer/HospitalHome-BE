from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.familiarSerializer import FamiliarSerializer
from HospitalHomeBE.models.familiar import Familiar

class FamiliarCrearView(views.APIView):
    def post(self, request, format=None):
        serializador=FamiliarSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response (serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        modelo=Familiar.objects.all()
        serializar=FamiliarSerializer(modelo, many=True)
        return Response (serializar.data)

class ConsultarFamiliarView (views.APIView):
    def put (self, request, pk, format=None):
        modelo=Familiar.objects.get(pk=pk)
        serializacion=FamiliarSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Familiar.objects.get(pk=pk)
        modelo.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        modelo=Familiar.objects.get(pk=pk)
        serializar= FamiliarSerializer(modelo)
        return Response (serializar.data)