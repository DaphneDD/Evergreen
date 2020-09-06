from rest_framework import serializers
from .models import Candidate, Test

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        #fields = ['id', 'first_name', 'last_name', 'id_type', 'id_number']
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    exam = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='duration'
    )
    #duration = serializers.TimeField('exam')
    class Meta:
        model = Test
        fields = ['id', 'exam_id','start_time', 'exam', 'status']
        #fields = ['id', 'exam_id','start_time', 'duration', 'status']
