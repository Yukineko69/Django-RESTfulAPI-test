from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name