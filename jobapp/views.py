from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):

    if request.user.role != "RECRUITER":
        return Response(
            {"error": "Only recruiters can post jobs"},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(company=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

    serializer = JobSerializer(job)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_job(request, pk):

    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

    if request.user != job.company:
        return Response({"error": "Not allowed"}, status=403)

    serializer = JobSerializer(job, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_job(request, pk):

    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

    if request.user != job.company:
        return Response({"error": "Not allowed"}, status=403)

    job.delete()
    return Response({"message": "Job deleted successfully"}, status=204)