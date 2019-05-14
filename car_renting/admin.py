from django.contrib import admin
from car_renting.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_available', 'name', 'registered_at', 'plate_number', 'price')

