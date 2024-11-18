from django.db import models
from documentation.models import Documentation


# Create your models here.

class Group(models.Model):
    """
    Группа - данные всех деталей. Группа входит в документ. В одном документе может быть несколько групп.
    """
    number = models.CharField(max_length=255, verbose_name="Номер группы")
    name = models.CharField(max_length=255, verbose_name="Название группы")
    documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE, verbose_name="Документация")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name
