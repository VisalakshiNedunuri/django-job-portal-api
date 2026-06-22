from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from users.permissions import IsRecruiter
from rest_framework.permissions import AllowAny
from .pagination import JobPagination



@api_view(["GET"])
def get_job_detail(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_jobs(request):
    jobs = Job.objects.all().order_by("-created_at")

    # Search
    search = request.GET.get("search")
    if search:
        jobs = jobs.filter(title__icontains=search)

    # Company
    company = request.GET.get("company")
    if company:
        jobs = jobs.filter(company__icontains=company)

    # Location
    location = request.GET.get("location")
    if location:
        jobs = jobs.filter(location__icontains=location)

    # Salary filters
    min_salary = request.GET.get("min_salary")
    if min_salary:
        jobs = jobs.filter(salary__gte=min_salary)

    max_salary = request.GET.get("max_salary")
    if max_salary:
        jobs = jobs.filter(salary__lte=max_salary)

    paginator = JobPagination()
    page = paginator.paginate_queryset(jobs, request)

    serializer = JobSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated,IsRecruiter])
def create_job(request):
    if not request.user.is_authenticated:
        return Response({"error": "Login required"}, status=401)

    serializer = JobSerializer(
        data=request.data,
        context={"request": request}
    )

    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data)

    return Response(serializer.errors)

'''
@api_view(["PUT"])
def update_job(request, pk):
    job = get_object_or_404(Job, id=pk)

    serializer = JobSerializer(job, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)'''

@api_view(["PUT"])
def update_job(request, pk):
    if not request.user.is_authenticated:
        return Response({"error": "Login required"}, status=401)

    job = get_object_or_404(Job, id=pk)

    if job.created_by != request.user:
        return Response({"error": "Not allowed"}, status=403)

    serializer = JobSerializer(job, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

'''
@api_view(["DELETE"])
def delete_job(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.delete()
    return Response({"message": "Job deleted successfully"})'''

@api_view(["DELETE"])
def delete_job(request, pk):
    if not request.user.is_authenticated:
        return Response({"error": "Login required"}, status=401)

    job = get_object_or_404(Job, id=pk)

    if job.created_by != request.user:
        return Response({"error": "Not allowed"}, status=403)

    job.delete()
    return Response({"message": "Job deleted"})