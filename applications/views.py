from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Application
from .serializers import ApplicationSerializer
from users.permissions import IsRecruiter
from jobs.models import Job
from .serializers import ApplicationStatusSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

'''
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_job(request):
    user = request.user

    #  block recruiter
    if user.role == "recruiter":
        return Response({"error": "Recruiters cannot apply"}, status=403)

    serializer = ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(applicant=user)
        return Response(serializer.data)

    return Response(serializer.errors, status=400)
'''

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_job(request):
    user = request.user

    if user.role == "recruiter":
        return Response({"error": "Recruiters cannot apply"}, status=403)

    job_id = request.data.get("job")

    #  prevent duplicate application
    if Application.objects.filter(job_id=job_id, applicant=user).exists():
        return Response(
            {"error": "You already applied for this job"},
            status=400
        )

    serializer = ApplicationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(applicant=user)
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_applications(request):
    user = request.user
    applications = Application.objects.filter(applicant=user).order_by('-applied_at')

    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_applicants(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

    # ONLY recruiter (job owner) can see applicants
    if job.created_by != request.user:
        return Response({"error": "Not allowed"}, status=403)

    applications = Application.objects.filter(job=job)
    serializer = ApplicationSerializer(applications, many=True)

    return Response({
        "job": job.title,
        "total_applicants": applications.count(),
        "applications": serializer.data
    })

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_application_status(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    # Ensure only the recruiter who posted the job can update
    if application.job.created_by != request.user:
        return Response(
            {"error": "You are not authorized."},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = ApplicationStatusSerializer(
        application,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)