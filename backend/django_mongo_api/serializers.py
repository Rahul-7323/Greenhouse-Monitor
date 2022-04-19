from rest_framework import serializers
from django_mongo_api.models import Test


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ('id', 'title', 'content')