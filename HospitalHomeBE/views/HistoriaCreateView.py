from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.historiaSerializer import HistoriaSerializer

class CrearHistclinicaView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = HistoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)