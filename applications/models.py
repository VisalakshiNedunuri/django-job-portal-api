from django.db import models
from users.models import User
from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shortlisted", "Shortlisted"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    cover_letter = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        
        default="Pending"
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "applicant")

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"