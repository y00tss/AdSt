from groups.models import Group
from documentation.models import Documentation
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    documentation = serializers.PrimaryKeyRelatedField(queryset=Documentation.objects.all())

    class Meta:
        model = Group
        fields = "__all__"
        depth = 1
