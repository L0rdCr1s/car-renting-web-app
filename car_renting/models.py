from django.db import models
from accounts.models import CustomUser

class Car(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name="car owner", on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=8)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=8)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    cover_image = models.ImageField(upload_to='cars/%Y/%m/%d/')
    registered_at = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    cars = models.Manager()

    def __str__(self):
        return self.name

class Booking(models.Model):

    BOOKING_STATUSES = [('requesting', 'requesting', ), ('accepted', 'accepted'), ('rejected', 'rejected')]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    booking_status = models.CharField(choices=BOOKING_STATUSES, default='requesting', max_length=30)
    booking_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    bookings = models.Manager()

    def __str__(self):
        return self.car.name
