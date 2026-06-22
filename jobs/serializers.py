from rest_framework import serializers
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    

    class Meta:
        model = Job
        fields = "__all__"