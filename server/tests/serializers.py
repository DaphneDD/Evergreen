from rest_framework import serializers
from .models import Candidate, Test

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    duration = serializers.TimeField(source='exam.duration')
    class Meta:
        model = Test
        fields = ['id', 'exam_id','start_time', 'duration', 'status']
