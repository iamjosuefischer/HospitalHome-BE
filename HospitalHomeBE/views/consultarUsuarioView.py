from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from HospitalHomeBE.models.usuario import Usuario
from HospitalHomeBE.serializers.usuarioSerializer import UserSerializer

class ConsultUserView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)