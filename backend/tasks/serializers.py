from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

