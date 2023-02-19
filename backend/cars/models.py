from django.db import models
from authentication.models import User
from django.utils.safestring import mark_safe
from PIL import Image as Im # new

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

def upload_to(instance, filename):
    return 'cars/{user}/{filename}'.format(user=instance.user, filename=filename)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='wise')
    make = models.CharField(max_length=30, blank=True, null=True, default='Make', help_text='Car Make')
    model = models.CharField(max_length=100, blank=True, null=True, default='Model', help_text='Car Model')
    year = models.IntegerField(default=2023, blank=True, null=True)

    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, default=None)
    
    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="200" height="200" />' % (self.photo))
    
    def save(self): # new
        super().save()
        img = Im.open(self.photo.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)