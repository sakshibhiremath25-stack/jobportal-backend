from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, serializers

from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer


# ==============================
# List and Create Jobs (Recruiter)
# ==============================
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Only recruiter can create jobs
        if not self.request.user.is_staff:
            raise serializers.ValidationError("Only recruiters can create jobs.")
        serializer.save(employer=self.request.user)


# ==============================
# Apply for Job (Candidate)
# ==============================
class ApplyJobView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        # Prevent duplicate applications
        if JobApplication.objects.filter(job=job, user=request.user).exists():
            return Response({"error": "Already applied"}, status=400)

        serializer = JobApplicationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(job=job, user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# ==============================
# Candidate → My Applications
# ==============================
class MyApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        applications = JobApplication.objects.filter(user=request.user)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)


# ==============================
# Employer → View Applications
# ==============================
class JobApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id, employer=request.user)
        except Job.DoesNotExist:
            return Response({"error": "Not authorized or job not found"}, status=403)

        applications = JobApplication.objects.filter(job=job)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)


# ==============================
# Employer → Accept / Reject Applications
# ==============================
class UpdateApplicationStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, application_id):
        try:
            application = JobApplication.objects.get(id=application_id)
        except JobApplication.DoesNotExist:
            return Response({"error": "Application not found"}, status=404)

        # Only employer of that job can update
        if application.job.employer != request.user:
            return Response({"error": "Not authorized"}, status=403)

        status_value = request.data.get("status")

        if status_value not in ["accepted", "rejected"]:
            return Response({"error": "Invalid status"}, status=400)

        application.status = status_value
        application.save()

        return Response({"message": "Status updated successfully"})