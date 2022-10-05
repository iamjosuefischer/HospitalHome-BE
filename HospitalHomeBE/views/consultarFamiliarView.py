from rest_framework import generics, status
from rest_framework.response import Response
from HospitalHomeBE.models.familiar import Familiar
from HospitalHomeBE.serializers.familiarSerializer import FamiliarSerializer
class ConsultFamiliarView(generics.RetrieveAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        