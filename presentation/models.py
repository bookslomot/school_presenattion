from django.db import models

from user.models import User


class Presentation(models.Model):

    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner')
    presentation = models.FileField(upload_to='presentation/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return f'Презентация - {self.owner}. Тема презентации - ({self.title})'
