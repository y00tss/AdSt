from django.db import models
from auth_custom.models import User


# Create your models here.
class Task(models.Model):
    """Task model"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
