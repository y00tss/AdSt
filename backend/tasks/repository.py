from typing import Optional, Dict, Any
from django.db.models.query import QuerySet
from .models import Task
from django.core.exceptions import ObjectDoesNotExist


class TaskRepository:
    """
    Repository for managing Task model objects.
    """

    @staticmethod
    def get_all_tasks(user_id: int) -> QuerySet[Task]:
        """Retrieve all tasks for a specific user."""
        return Task.objects.filter(user=user_id)

    @staticmethod
    def create_task(data: Dict[str, Any]) -> Task:
        """Create a new task."""
        return Task.objects.create(**data)

    @staticmethod
    def get_task_by_id(task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        try:
            return Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_task(task: Task, data: Dict[str, Any]) -> Task:
        """Update an existing task with the given data."""
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task: Task) -> None:
        """Delete a task."""
        task.delete()

    @staticmethod
    def change_status(task: Task, status: bool = True) -> Task:
        """Mark a task as completed or not completed."""
        task.is_completed = status
        task.save()
        return task
