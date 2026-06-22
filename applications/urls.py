from django.urls import path
from .views import apply_job,my_applications,job_applicants,update_application_status

urlpatterns = [
    path("apply/", apply_job),
    path("my/", my_applications),
    path("job/<int:job_id>/applications/", job_applicants),
    path("<int:application_id>/status/", update_application_status),
    
]