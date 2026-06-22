from rest_framework import serializers
from .models import Application
from jobs.models import Job



class JobMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'company', 'location','salary']


''

class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all()
    )

    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ["applicant","status", "applied_at"]


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']