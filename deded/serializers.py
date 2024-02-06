from rest_framework import serializers 
from .models import dede

class dedeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = dede 
        fields = '__all__' 
