from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.pSaludSerializer import PerSaludSerializer

class CrearPSaludView(views.APIView):
    def post(self, request):
        serializer = PerSaludSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 