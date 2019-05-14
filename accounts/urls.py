from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.user_login),
    path('normalregistration', views.normal_registration),
    path('register', views.custom_user_register),
    path('confirm/<int:id>', views.confirm_account),
    path('activate/account', views.activate_account),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)