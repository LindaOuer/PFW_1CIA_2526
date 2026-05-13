from rest_framework import serializers
from .models import Classe

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'
        read_only_fields = ['id']