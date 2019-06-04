from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login),
    path('login', views.user_login, name='login'),
    path('userregistration', views.user_registration, name='registration'),
    path('logout', views.user_logout, name='logout'),
    path('settings', views.settings, name="settings"),
    path('update/user/passowrd/<int:id>', views.update_password, name="password_update"),
    path('update/user/profile/<int:id>', views.update_profile, name="profile_update")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)