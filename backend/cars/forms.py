from django import forms
from .models import Car

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['photo', 'image_url', 'make', 'model', 'year', 'user', 'id']