from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.historiaSerializer import HistoriaSerializer
from HospitalHomeBE.models.historia import Historia

class HistoriaCrearView(views.APIView):
    def post(self, request, format=None):
        serializador=HistoriaSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response (serializador.errors, status=status.HTTP_400_BAD_REQUEST)
class ConsultarHistoriaView (views.APIView):
    def put (self, request, pk, format=None):
        modelo=Historia.objects.get(pk=pk)
        serializacion=HistoriaSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Historia.objects.get(pk=pk)
        modelo.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        modelo=Historia.objects.get(pk=pk)
        serializar= HistoriaSerializer(modelo)
        return Response (serializar.data)