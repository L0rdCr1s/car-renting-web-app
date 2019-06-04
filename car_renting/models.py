from django.db import models
from accounts.models import CustomUser

class Car(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name="car owner", on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=8)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=12)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    cover_image = models.ImageField(upload_to='cars/%Y/%m/%d/')
    registered_at = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    cars = models.Manager()

    def __str__(self):
        return self.name


class CarImage(models.Model):

    car = models.ForeignKey(Car, related_name="car_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/images/%Y/%m/%d/')

    images = models.Manager()

    def __str__(self):
        return self.car.name

class Booking(models.Model):

    BOOKING_STATUSES = [
        ('requesting', 'requesting', ),
        ('accepted', 'accepted'), 
        ('rejected', 'rejected'),
        ('canceled', 'canceled')
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    booking_status = models.CharField(choices=BOOKING_STATUSES, default='requesting', max_length=30)
    booking_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    booked_at = models.DateTimeField(auto_now_add=True)

    bookings = models.Manager()

    def __str__(self):
        return self.car.name

class Notification(models.Model):

    target = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    source = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=2, related_name="source")
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=300)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, related_name="notifications", null=True)
    is_viewed = models.BooleanField(default=False)

    notifications = models.Manager()

    def __str__(self):
        return self.message

class BookingHistory(models.Model):

    car = models.ForeignKey(Car, related_name='booking_history', on_delete=models.CASCADE, unique=False)
    user = models.ForeignKey(CustomUser, related_name='renters', on_delete=models.CASCADE, unique=False)
    status = models.CharField(max_length=255, default="canceled")
    booked_at = models.DateTimeField(auto_now_add=True)

    history = models.Manager()

    def __str__(self):
        return self.user.get_full_name()

class PaymentRecord(models.Model):

    booking = models.ForeignKey(Booking, related_name='payments', on_delete=models.CASCADE)
    payer = models.ForeignKey(CustomUser, related_name='payers', on_delete=models.CASCADE)
    payee = models.ForeignKey(CustomUser, related_name='payees', on_delete=models.CASCADE) 
    amount = models.CharField(max_length=20)
    payment_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amount