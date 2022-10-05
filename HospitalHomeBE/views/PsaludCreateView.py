from rest_framework import status, views
from rest_framework.response import Response
from HospitalHomeBE.serializers.psaludSerializer import PersonalSaludSerializer

class CrearPsaludView(views.APIView):
    def post(self, request,*args, **kwargs):
        serializer = PersonalSaludSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)