from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *


class UserAdmin(BaseUserAdmin):

    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('first_name', 'email', 'last_name', 'date_joined')
    list_filter = ('first_name', 'last_name', 'date_joined')

    # fields that will be editable when user info has to be updated
    fieldsets = (
        ('Login Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_login',)


# register our custom user model and user admin model
admin.site.register(CustomUser, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_contact', 'date_of_birth', 'booked_cars', 'owned_cars')
    list_filter = ('mobile_contact', 'booked_cars', 'owned_cars')

admin.site.register(UserProfile, ProfileAdmin)



## admin page customizations
admin.sites.AdminSite.site_header = "Car renting System administration"
admin.sites.AdminSite.site_title = "Admin Page"
