from rest_framework import viewsets, status

from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework.permissions import AllowAny


class GroupsView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny, ]  # TODO убрать AllowAny
