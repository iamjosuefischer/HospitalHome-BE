from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.sigvitalesSerializer import SignosVitalesSerializers


class CrearSigvitalesView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignosVitalesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)