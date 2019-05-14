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

    # check if user has booked this car
    booking = Booking.bookings.filter(car=car).filter(booking_user=request.user).filter(booking_status='requesting')
    
    
    if booking is not None:
        user_has_booked_it = True
        print(user_has_booked_it)
    else:
        user_has_booked_it = False


    context = {
        'car': car,
        'media': settings.MEDIA_URL,
        'view_type': 'car_details',
        'user_has_booked_it': user_has_booked_it
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
        
        booking = Booking.bookings.create(car = car, booking_user = request.user)
        booking.save()
        return redirect('/car_renting/car/%s'%(id))


def cancel_request(request, id):

    if request.user.is_authenticated:
        try:
            booking_request = Booking.bookings.get(car__id=id)
            if booking_request.booking_user.id != request.user.id:
                return HttpResponseNotFound('booking not found')
            booking_request.delete()
        except Booking.DoesNotExist:
            return HttpResponseNotFound('booking record not found')
    return redirect('/car_renting/car/%s'%(id))