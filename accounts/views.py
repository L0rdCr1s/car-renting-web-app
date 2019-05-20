from django.shortcuts import render, get_object_or_404
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views
from .models import *
from django.contrib.auth import logout
from django.conf import settings
from car_renting.models import Notification

def user_login(request):
    fresh_form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['email'], password=data['password'])
            if user is not None:
                if user.is_active:
                    request.session['username'] = user.email
                    login(request, user)
                    return redirect('/car_renting/home')
                else:
                    context = {
                        'with_status' : True,
                        'title': 'Failed!!',
                        'info' : 'account disabled',
                        'static_url': settings.STATIC_URL,
                        'alert': 'alert-danger'
                    }
                    return render(request, 'login.html', context)
            else:
                context = {
                    'with_status' : True,
                    'title': 'Failed!!',
                    'info' : 'invalid user name or password',
                    'static_url': settings.STATIC_URL,
                    'alert': 'alert-danger'
                }
                return render(request, 'login.html', context)
        else:
            context = {
                'with_status' : True,
                'title': 'Failed!!',
                'info' : 'invaild data provided',
                'static_url': settings.STATIC_URL,
                'alert': 'alert-danger'
            }
            return render(request, 'login.html', context)
    else:
        static_url = settings.STATIC_URL

        # if user is authenticated bypass the login page
        if request.user.is_authenticated:
            return redirect('/car_renting/home')
            
        return render(request, 'login.html', {'form': fresh_form, 'static_url': static_url})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')

def user_registration(request):

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data['password2'])
            user.save()

            new_user = UserProfile(user=user)
            new_user.save()

            context = {
                'with_status' : True,
                'title': 'Success',
                'info' : 'you have successfully registered',
                'alert': 'alert-success',
                'static_url': settings.STATIC_URL
            }
            return render(request, 'Registration/register.html', context)
        else:
            context = {
                'with_status' : True,
                'title': 'Failed',
                'info' : 'Invalid data provided, please check your input',
                'static_url': settings.STATIC_URL,
                'alert': 'alert-danger'
            }
            return render(request, 'Registration/register.html', context)
    else:
        form = forms.RegisterForm()
        static_url = settings.STATIC_URL
        return render(request, 'Registration/register.html', {"form": form, 'static_url': static_url})


def settings(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            # check for unread notifications
            notifications = Notification.notifications.filter(target__id=request.user.id).order_by('-created_at')
            navbar_notifications = notifications.filter(is_viewed=False)

            context = {
                'user': request.user,
                'view_type': 'settings',
                'navbar_notifications': navbar_notifications,

                # these two settings variables are hard coded because due to some
                # an uknown error settings is detected as a function with no attributes 
                # MEDIA_URL nor STATIC_URL, fix it if you have time, i'm sleepy at the time of this writting
                'media': 'media/',
                'static_url': 'static/'
            }
            return render(request, 'home.html', context)

        elif request.method == "POST":
            pass