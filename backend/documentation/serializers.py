from documentation.models import Documentation
from rest_framework import serializers


class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'
