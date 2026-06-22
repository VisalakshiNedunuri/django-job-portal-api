from django.urls import path
from .views import create_job, get_jobs, get_job_detail,update_job,delete_job

urlpatterns = [
    path("create/", create_job),
    path("", get_jobs),
    path("<int:pk>/", get_job_detail),
    path("<int:pk>/update/", update_job),
     path("<int:pk>/delete/", delete_job),
]