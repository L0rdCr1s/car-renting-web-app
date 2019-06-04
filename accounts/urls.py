from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login),
    path('login', views.user_login, name='login'),
    path('userregistration', views.user_registration, name='registration'),
    path('logout', views.user_logout, name='logout'),
    path('settings', views.settings, name="settings")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)