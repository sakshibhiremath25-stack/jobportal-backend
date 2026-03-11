from rest_framework import serializers
from .models import Job, JobApplication


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