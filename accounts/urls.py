from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.user_login),
    path('userregistration', views.user_registration),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)