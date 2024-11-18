from django.db import models

# Create your models here.


class Documentation(models.Model):
    """
    Документация, под нее цепляются группы.
    """
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Документация"
        verbose_name_plural = "Документации"

    def __str__(self):
        return self.title
