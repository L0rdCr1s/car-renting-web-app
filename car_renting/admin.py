from django.contrib import admin
from car_renting.models import Car, Booking, Notification, BookingHistory, CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_available', 'name', 'registered_at', 'plate_number', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('car', 'booking_user', 'booking_status')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('target', 'created_at', 'booking', 'message')

@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'booked_at')

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', )

