from rest_framework import serializers
from .models import Job, JobApplication
from .models import ScreeningQuestion, CandidateAnswer

class ScreeningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningQuestion
        fields = "__all__"


class CandidateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateAnswer
        fields = "__all__"


# =========================
# Job Serializer
# =========================
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# =========================
# Job Application Serializer
# =========================
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['user', 'job', 'applied_at']