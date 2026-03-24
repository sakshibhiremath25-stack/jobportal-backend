from rest_framework import generics, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import JobApplication, Job
from .serializers import JobApplicationSerializer, JobSerializer


# 🔹 List all jobs or create job
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise serializers.ValidationError("Only recruiters can create jobs.")
        serializer.save(employer=self.request.user)


# 🔹 Candidate: View applied jobs
class CandidateAppliedJobsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)


# 🔹 Employer: View applicants for a job
class EmployerApplicationsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']

        return JobApplication.objects.filter(
            job_id=job_id,
            job__employer=self.request.user   # ✅ restrict to owner
        )


# 🔹 Candidate: Apply for a job
class ApplyJobView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        user = self.request.user

        if JobApplication.objects.filter(user=user, job=job).exists():
            raise serializers.ValidationError("You have already applied for this job.")

        serializer.save(user=user)


# 🔹 Employer: Update application status
class UpdateApplicationStatusView(generics.UpdateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        application = self.get_object()

        if application.job.employer != self.request.user:
            raise PermissionDenied("You are not allowed to update this application")

        serializer.save()
        