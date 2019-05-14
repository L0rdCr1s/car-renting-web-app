from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *


class UserAdmin(BaseUserAdmin):

    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # fields that will be displayed on the users list
    list_display = ('first_name', 'email', 'last_name', 'last_login', 'date_joined')

    # fields that will be used to filter the users on the users list
    list_filter = ('first_name', 'last_name', 'date_joined', 'last_login')

    # fields that will be editable when user info has to be updated
    fieldsets = (
        ('Login Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'is_a_results_manager', 'is_a_club',
                                    'is_a_driver', 'is_a_navigator', 'is_iaa_account', 'has_news_access',
                                    'has_media_access', 'groups'
                                    )}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )

    # this creates the search  form that will search users by their info
    search_fields = ('email', 'first_name', 'last_name')

    # list of users will be ordered by their last login time
    ordering = ('last_login',)


# register our custom user model and user admin model
admin.site.register(CustomUser, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):

    # fields that will be displayed on the users list
    list_display = ('user',)

    # fields that will be used to filter the users on the users list
    list_filter = ('user',)

admin.site.register(UserProfile, ProfileAdmin)


@admin.register(SystemInfo)
class SystemInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    readonly_fields = ('images_count', 'videos_count', 'news_count', 'users_count')


@admin.register(IaaRegistered)
class IaaRegisteredAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license_number', 'type', 'door_number')
    search_fields = ('first_name', 'last_name', 'license_number')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(DriverNavigator)
class DriverNavigatorAdmin(admin.ModelAdmin):
    list_display = ('driver', 'license_number', 'team', 'nationality', 'type')
    search_fields = ('driver', 'license_number', 'team')

@admin.register(CarPhotos)
class CarPhotosAdmin(admin.ModelAdmin):
    list_display = ('driverNavigator', )

@admin.register(Attachments)
class CarPhotosAdmin(admin.ModelAdmin):
    list_display = ('driverNavigator', 'name', 'file', )

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(ClubRequestingForRegistration)
class ClubRequestingForRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_registerd')



## admin page customizations
admin.sites.AdminSite.site_header = "Rally Tanzania administration"
admin.sites.AdminSite.site_title = "Rally admin"
