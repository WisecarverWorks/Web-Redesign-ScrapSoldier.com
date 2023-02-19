from django.contrib import admin
from .models import Car

class imageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'make', 'model', 'year', 'photo', 'image_url')

# Register your models here.
admin.site.register(Car, imageAdmin)
