from django.contrib import admin
from BackgroundPredictor.models import InputImage

# Register your models here.

class InputImageAdmin(admin.ModelAdmin):
    fields = ['image', 'trimap', 'output_trimap', 'foreground_image']

admin.site.register(InputImage, InputImageAdmin)