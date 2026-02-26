from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):

    # Allow only RECRUITER to post jobs
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
