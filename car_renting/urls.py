from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('car/<int:id>', views.car_details, name="car_details"),
    path('deletecar/<int:id>', views.delete_car, name="delete_car"),
    path('changecarstatus/<int:id>', views.change_car_status, name="change_car_status"),
    path('bookacar/<int:id>', views.book_a_car, name="book_a_car"),
    path('cancelrequest/<int:id>', views.cancel_request, name="cancel_request"),
    path('notifications', views.get_notifications, name="notifications"),
    path('replybooking/<int:id>/<int:action>', views.accept_booking, name='reply_booking'),
    path('userprofile/<int:id>/<int:section_type>', views.get_user_profile, name="user_profile"),
    path('account/<int:section_type>', views.show_my_account, name='account')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
