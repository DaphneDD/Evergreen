from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    id_type = serializers.CharField(max_length=255)
    id_number = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Candidate.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.id_type = validated_data.get('id_type', instance.id_type)
        instance.id_number = validated_data.get('id_number', instance.id_number)
        instance.save()
        return instance

