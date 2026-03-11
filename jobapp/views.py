from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplication, Job
from .serializers import JobApplicationSerializer, JobSerializer


# List all jobs or create a new job (GET + POST)
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Only allow recruiters to create jobs
        if not self.request.user.is_staff:  # or use a custom field like is_recruiter
            raise serializers.ValidationError("Only recruiters can create jobs.")
        serializer.save(employer=self.request.user)


# Candidate: view jobs they applied for
class MyApplicationsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)


# Recruiter: view applications for a specific job
class JobApplicationsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return JobApplication.objects.filter(job_id=job_id)


# Candidate: apply for a job
class ApplyJobView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        user = self.request.user

        if JobApplication.objects.filter(user=user, job=job).exists():
            raise serializers.ValidationError("You have already applied for this job.")

        serializer.save(user=user)
        