from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskStatusChangeSerializer

from tasks.repository import TaskRepository


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    repository = TaskRepository

    def list(self, request):
        tasks = self.repository.get_all_tasks(user_id=self.request.user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = self.repository.create_task(serializer.validated_data)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        task = self.repository.get_task_by_id(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        task = self.repository.get_task_by_id(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        TaskRepository.delete_task(task)
        return Response({"status": "Task deleted"}, status=status.HTTP_204_NO_CONTENT)


class TaskStatusChangeViewSet(viewsets.ViewSet):
    repository = TaskRepository
    serializer_class = TaskStatusChangeSerializer

    @action(detail=True, methods=['post'])
    def task_status(self, request, pk=None):
        task = self.repository.get_task_by_id(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        task = self.repository.change_status(task, request.data.get('is_completed'))
        return Response(TaskSerializer(task).data)
