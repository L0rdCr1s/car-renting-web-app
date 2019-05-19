from django.shortcuts import render, redirect
from accounts.models import CustomUser, UserProfile
from car_renting.models import Car, Booking, Notification, BookingHistory
from django.conf import settings
from django.http import HttpResponseNotFound
import random
from accounts.forms import NewCarForm

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
                return redirect('/car_renting/account/1')
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


# set the car available or unavailable for booking
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
        
        # if Booking.bookings.filter(car=car, booking_user=request.user).exists():
        #     booking = Booking.bookings.get(car=car)
        #     booking.booking_status = 'requesting'
        # else:
        #     booking = Booking.bookings.create(car = car, booking_user = request.user)

        booking = Booking.bookings.create(car = car, booking_user = request.user)
        booking.save()

        # notify owner of the car for this booking
        notification = Notification.notifications.create(
            target = car.user,
            source = request.user,
            message = "Hello!! is requesting to rent your car",
            booking = booking
        )
        notification.save()

        return redirect('/car_renting/car/%s'%(id))
    else:
        return redirect('/login')


def cancel_request(request, id):

    if request.user.is_authenticated:
        try:
            booking_request = Booking.bookings.get(car__id=id, booking_user=request.user)
            if booking_request.booking_user.id != request.user.id:
                return HttpResponseNotFound('booking not found')
            # booking_request.booking_status = 'canceled'
            # booking_request.save()

            # record this event and then delete it in the booking list
            booking_history = BookingHistory.history.create(car=booking_request.car, user=booking_request.booking_user)
            booking_history.save()

            booking_request.delete()
            return redirect('/car_renting/car/%s'%(id))
            
        except Booking.DoesNotExist:
            return HttpResponseNotFound('booking record not found')
    else:
        return redirect('/login')


def get_notifications(request):

    if request.user.is_authenticated:

        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        for notification in notifications:
            notification.is_viewed = True
            notification.save()

        context = {
            'view_type': 'notifications',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')


def reply_booking(request, id, action):
    if request.user.is_authenticated:
        try:
            notification = Notification.notifications.get(pk=id)
            if notification.target.id == request.user.id:
                notification.is_viewed = True

                # change the status of the booking request
                if action == 1:
                    message = "%s has accepted your request for %s"%(request.user.get_full_name(), notification.booking.car.name)

                    # make the car unavailable after accepting a request
                    notification.booking.car.is_available = False
                    notification.booking.car.save()

                    # record this event and then delete it in the booking list
                    booking_history = BookingHistory.history.create(
                                car=notification.booking.car, 
                                user=notification.booking.booking_user, 
                                status="accepted"
                            )
                    booking_history.save()
                    notification.save()

                elif action == 0:
                    message = "%s has rejected your request for %s"%(request.user.get_full_name(), notification.booking.car.name)

                    # record this event and then delete it in the booking list
                    booking_history = BookingHistory.history.create(
                                car=notification.booking.car, 
                                user=notification.booking.booking_user, 
                                status="rejected"
                            )
                    booking_history.save() 
                    notification.save()

                else:
                    return HttpResponseNotFound('invalid action provided')

                # notify a person who sent the request for this reply
                repy_notification = Notification.notifications.create(
                    target = notification.source,
                    source = request.user,
                    message = message,
                    booking = notification.booking
                )
                repy_notification.save()

                # delete the event from booking list to allow another entry with the same entity 
                # to be saved without intergrity error
                Booking.bookings.get(pk=notification.booking.id).delete()

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
        user_booking_history = BookingHistory.history.filter(user=user)
        user_vehicles = Car.cars.filter(user=user)

        context = {
            'view_type': 'profile',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
            'user': user,
            'user_bookings': user_bookings,
            'user_booking_history': user_booking_history,
            'user_vehicles': user_vehicles,
            'section_type': section_type
        }
        return render(request, 'home.html', context)
    else:
        return redirect('/login')

def show_my_account(request, section_type):

    if request.user.is_authenticated:

        notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
        navbar_notifications = notifications.filter(is_viewed=False)

        user_bookings = Booking.bookings.filter(booking_user=request.user)
        user_vehicles = Car.cars.filter(user=request.user)
        user_booking_history = BookingHistory.history.filter(user=request.user)

        context = {
            'view_type': 'account',
            'navbar_notifications': navbar_notifications,
            'media': settings.MEDIA_URL,
            'notifications': notifications,
            'user_bookings': user_bookings,
            'user_vehicles': user_vehicles,
            'user_booking_history': user_booking_history,
            'section_type': section_type,
        }

        if request.method == 'GET':
            return render(request, 'home.html', context)
        else:
            form = NewCarForm(request.POST)
            if form.is_valid():
                form.save(request.user.id)

                context.update( {
                    # return with an error
                    'with_status': True,
                    'alert': 'alert-success',
                    'title': 'Success!! ,',
                    'info': 'car added successfully'
                })
                return render(request, 'home.html', context)
            else:
                context.update( {
                    # return with an error
                    'with_status': True,
                    'alert': 'alert-danger',
                    'title': 'Failed to add car,',
                    'info': 'check your input and try again' 
                })
                return render(request, 'home.html', context)
    else:
        return redirect('/login')