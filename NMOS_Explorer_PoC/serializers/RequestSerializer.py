from rest_framework import serializers
from NMOS_Explorer_PoC.models import Request;

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'