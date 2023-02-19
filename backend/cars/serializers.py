from rest_framework import serializers
from .models import Car

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'user', 'make', 'model', 'year', 'photo', 'image_url']
        depth = 1
