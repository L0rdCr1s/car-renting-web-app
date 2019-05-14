from django.shortcuts import render, redirect
from accounts.models import CustomUser, UserProfile
from car_renting.models import Car, Booking
from django.conf import settings
from django.http import HttpResponseNotFound

def home(request):

    # get all cars with the status available
    cars = Car.cars.filter(is_available=True).order_by('-registered_at')

    context = {
        'user': request.user,
        'static_url' : settings.STATIC_URL,
        'media': settings.MEDIA_URL,
        'view_type': 'home',
        'cars': cars
    }
    return render(request, 'home.html', context)

def car_details(request, id):

    # car information
    try:
        car = Car.cars.get(pk=id)
    except Car.DoesNotExist:
        return HttpResponseNotFound('Car not found')

    context = {
        'car': car,
        'media': settings.MEDIA_URL,
        'view_type': 'car_details'
    }
    
    return render(request, 'home.html', context)

def delete_car(request, id):

    if request.user.is_authenticated:
        try:
            car = Car.cars.get(pk=id)
            if request.user.id == car.user.id:
                car.delete()
            else:
                return HttpResponseNotFound('user not authorised')
        except Car.DoesNotExist:
            return HttpResponseNotFound('Car not found')
    else:
        return HttpResponseNotFound('user not authorised')
    
    context = {
        'car': car,
        'media': settings.MEDIA_URL,
        'view_type': 'home'
        }
        
    return render(request, 'home.html', context)

def change_car_status(request, id):

    try:
        car = Car.cars.get(pk=id)
    except Car.DoesNotExist:
        return HttpResponseNotFound('Car not found')

    if request.user.is_authenticated:
        if car.user.id == request.user.id:
            if car.is_available is True:
                car.is_available = False
                car.save()
            else:
                car.is_available = True
                car.save()
        else:
            return HttpResponseNotFound('user not authorised change status')
    else:
        return HttpResponseNotFound('user is not authenticated')
    return redirect('/car_renting/car/%s'%(id))


def book_a_car(request, id):

    if request.user.is_authenticated:
        try:
            car = Car.cars.get(pk=id)
        except Car.DoesNotExist:
            return HttpResponseNotFound('car not found')

        if car.user.id == request.user.id:
            return HttpResponseNotFound('you can not book your own car')
        
        booking = Booking.create(car = car, booking_user = request.user )