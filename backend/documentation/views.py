from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response

from documentation.models import Documentation
from documentation.serializers import DocumentationSerializer
from rest_framework.permissions import AllowAny


class DocumentationView(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    permission_classes = [AllowAny, ] #TODO убрать AllowAny

