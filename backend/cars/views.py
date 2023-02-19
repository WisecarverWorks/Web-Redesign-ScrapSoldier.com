from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Car
from .serializers import CarSerializer
from .forms import ImageUploadForm

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

# Create your views here.
def index(request):
    data = Car.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

# new
def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_cars(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cars = Car.objects.filter(user_id=request.user.id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
