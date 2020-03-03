from django.db import models
from django.utils import timezone

from manager.const import STATUS_CHOICES


class Task(models.Model):

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    deadline = models.DateField(default=timezone.now)
    description = models.TextField()
    file = models.FileField(null=True, upload_to=f'attachments/')

    def __str__(self):
        return f'{self.name.capitalize()}'

    def create_file_name(self):
        return f'{self.name}_{self.deadline}'
