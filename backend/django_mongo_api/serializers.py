from rest_framework import serializers
from django_mongo_api.models import Test, Sensor


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'title', 'content')
        
        
class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = (
            'id',
            'temperature',
            'moisture',
            'humidity',
            'air_vent',
            'water_pump'
        )