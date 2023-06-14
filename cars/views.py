from django.shortcuts import render
from .models import Car
def cars(request):
    cars = Car.objects.all()
    data = {
        'cars': cars,
    }
    return render(request, 'cars/cars.html')
