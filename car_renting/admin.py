from django.contrib import admin
from car_renting.models import Car, Booking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_available', 'name', 'registered_at', 'plate_number', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('car', 'booking_user', 'booking_status')
