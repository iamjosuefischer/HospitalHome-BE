from pyexpat import model
from HospitalHomeBE.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'perfil', 'name', 'telefono', 'genero')