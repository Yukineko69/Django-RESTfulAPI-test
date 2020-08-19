from django.db import models
from django.conf import settings

# Create your models here.
class InputImage(models.Model):
    image = models.ImageField(blank=False, null=False)
    trimap = models.ImageField(blank=False, null=False)

    output_trimap = models.ImageField(blank=True, null=True)
    foreground_image = models.ImageField(blank=True, null=True)    

    def __str__(self):
        return self.image.name
