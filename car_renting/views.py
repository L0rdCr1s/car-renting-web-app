from django.shortcuts import render, redirect
from accounts.models import CustomUser, UserProfile
from car_renting.models import Car, Booking, Notification
from django.conf import settings
from django.http import HttpResponseNotFound
import random

def home(request):

    if request.user.is_authenticated:
        # get all cars with the status available
        cars = Car.cars.filter(is_available=True).order_by('-registered_at')

        # check for unread notifications
        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        context = {
            'user': request.user,
            'static_url' : settings.STATIC_URL,
            'media': settings.MEDIA_URL,
            'view_type': 'home',
            'navbar_notifications': navbar_notifications,
            'cars': cars
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')

def car_details(request, id):
    if request.user.is_authenticated:

        # car information
        try:
            car = Car.cars.get(pk=id)
        except Car.DoesNotExist:
            return HttpResponseNotFound('Car not found')

        # check if user has booked this car
        user_has_booked_it = Booking.bookings.filter(car=car).filter(booking_user=request.user).filter(booking_status='requesting')
        
        # check for unread notifications
        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        context = {
            'car': car,
            'media': settings.MEDIA_URL,
            'view_type': 'car_details',
            'navbar_notifications': navbar_notifications,
            'user_has_booked_it': user_has_booked_it
        }
        
        return render(request, 'home.html', context)
    else:
        return redirect('/login')

def delete_car(request, id):

    if request.user.is_authenticated:

        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        if navbar_notifications is None:
            has_new_notification = "yes"
        else:
            has_new_notification = "no"

        try:
            car = Car.cars.get(pk=id)
            if request.user.id == car.user.id:
                car.delete()
            else:
                return HttpResponseNotFound('user not authorised')
        except Car.DoesNotExist:
            return HttpResponseNotFound('Car not found')
    else:
        return redirect('/login')
    
    context = {
        'car': car,
        'media': settings.MEDIA_URL,
        'navbar_notifications': navbar_notifications,
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
        return redirect('/login')
        
    return redirect('/car_renting/car/%s'%(id))


def book_a_car(request, id):

    if request.user.is_authenticated:
        try:
            car = Car.cars.get(pk=id)
        except Car.DoesNotExist:
            return HttpResponseNotFound('car not found')

        if car.user.id == request.user.id:
            return HttpResponseNotFound('you can not book your own car')
        
        if Booking.bookings.filter(car=car, booking_user=request.user).exists():
            booking = Booking.bookings.get(car=car)
            booking.booking_status = 'requesting'
        else:
            booking = Booking.bookings.create(car = car, booking_user = request.user)

        booking.save()
        return redirect('/car_renting/car/%s'%(id))
    else:
        return redirect('/login')


def cancel_request(request, id):

    if request.user.is_authenticated:
        try:
            booking_request = Booking.bookings.get(car__id=id, booking_user=request.user, booking_status='requesting')
            if booking_request.booking_user.id != request.user.id:
                return HttpResponseNotFound('booking not found')
            booking_request.booking_status = 'canceled'
            booking_request.save()
            return redirect('/car_renting/car/%s'%(id))
            
        except Booking.DoesNotExist:
            return HttpResponseNotFound('booking record not found')
    else:
        return redirect('/login')

def get_notifications(request):

    if request.user.is_authenticated:

        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        context = {
            'view_type': 'notifications',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')

def accept_booking(request, id, action):
    if request.user.is_authenticated:
        try:
            notification = Notification.notifications.get(pk=id)
            if notification.target.id == request.user.id:
                notification.is_viewed = True

                # change the status of the booking request
                if action == 1:
                    notification.booking.booking_status = "accepted"
                    notification.booking.save()
                elif action == 0:
                    notification.booking.booking_status = "rejected"
                    notification.booking.save()
                else:
                    return HttpResponseNotFound('invalid action provided')
                notification.save()
                return redirect('/car_renting/notifications')
                
            else:
                return HttpResponseNotFound('you can not update a notification that is not yours')
        except Notification.DoesNotExist:
            return HttpResponseNotFound('notification is not found')
    else:
        return redirect('/login')

def get_user_profile(request, id, section_type):
    if request.user.is_authenticated:
        try:
            user = CustomUser.users.get(pk=id)
        except objectDoesNotExist:
            return HttpResponseNotFound('user is not found')
        
        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        user_bookings = Booking.bookings.filter(booking_user=user)
        user_vehicles = Car.cars.filter(user=user)

        context = {
            'view_type': 'profile',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
            'user': user,
            'user_bookings': user_bookings,
            'user_vehicles': user_vehicles,
            'section_type': section_type
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')

def show_my_account(request, section_type):
    if request.user.is_authenticated:

        user_bookings = Booking.bookings.filter(booking_user=request.user)
        user_vehicles = Car.cars.filter(user=request.user)

        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        context = {
            'view_type': 'account',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
            'user_bookings': user_bookings,
            'user_vehicles': user_vehicles,
            'section_type': section_type
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')