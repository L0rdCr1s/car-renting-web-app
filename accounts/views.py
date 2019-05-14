# from django.shortcuts import render, get_object_or_404
# from . import forms
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout, views
# from django.core.mail import send_mail
# import random
# import datetime
# from django.utils import timezone
# from .models import *
# from django.contrib.auth import logout
# from django.contrib.auth import logout
# from django.db.utils import IntegrityError
# from django.conf import settings

# # imports for iaa registration
# from newsmedia.serializers import get_serializer, serialize_queryset
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status


# def show_auth_error(request, form, email, message, template, **kwargs):

#     context = {
#         "type": 0,
#         'form': form,
#         "error_title": "ACCESS DENIED!",
#         "error_info": message,
#         "email": email,
#         "action": kwargs['action']
#     }
#     return render(request, template, context)


# def get_user_direction(request, user, form, data):
#     if user.has_news_access or user.has_media_access or user.is_a_results_manager:
#         if user.is_staff:
#             request.session['username'] = user.email
#             login(request, user)
#             return redirect('/admin')
#         else:
#             message = "User not verified"
#             template = 'authentication/login.html'
#             return show_auth_error(request, form, data['email'], message, template, action=None)
#     elif user.is_iaa_account:
#         request.session['username'] = user.email
#         login(request, user)
#         return redirect('iaa/')
#     elif user.is_a_driver or user.is_a_navigator:
#         request.session['username'] = user.email
#         login(request, user)
#         return redirect('../driver_navigator_profile')
#     else:
#         message = "user not verified for login"
#         template = 'authentication/login.html'
#         return show_auth_error(request, form, data['email'], message, template, action=None)


# def go_to_user_account(request):
#     if request.user.is_authenticated:
#         if request.user.is_staff:
#             return redirect('../admin')
#         elif request.user.is_iaa_account:
#             return redirect('../iaa')
#         elif request.user.is_a_driver or request.user.is_a_navigator:
#             return redirect('../driver_navigator_profile')
#         else:
#             return redirect('../')
#     else:
#         return redirect('../')


# def user_login(request):
#     fresh_form = forms.LoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 username=data['email'], password=data['password'])
#             if user is not None:
#                 if user.is_active:
#                     return get_user_direction(request, user, fresh_form, data)
#                 else:
#                     message = "account is disabled"
#                     template = 'authentication/login.html'
#                     return show_auth_error(request, fresh_form, data['email'], message, template, action=None)
#             else:
#                 message = "invalid username or password"
#                 template = 'authentication/login.html'
#                 return show_auth_error(request, fresh_form, data['email'], message, template, action=None)
#         else:
#             message = "please provide a clean username and a clean password"
#             template = 'authentication/login.html'
#             return show_auth_error(request, fresh_form, "", message, template, action=None)
#     else:
#         return render(request, 'authentication/login.html', {'form': fresh_form, 'type': 1})


# def user_logout(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect('..')
#     else:
#         return redirect('..')


# # this method registers news, media and results guys
# def normal_registration(request):
#     form = forms.RegisterForm()
#     return render(request, 'registration/register.html', {"form": form})


# def custom_user_register(request):

#     if request.method == 'POST':
#         form = forms.RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password2'])
#             user.save()

#             # creating activation key and save it together with the user
#             # x is to differentiate between keys of unactivated users
#             x = datetime.datetime.today()
#             activation_key = random.randint(
#                 1, 1000) + x.year + x.month + x.day + x.hour + x.minute + x.second
#             key_expires = datetime.datetime.today() + datetime.timedelta(2)

#             new_user = UserProfile(
#                 user=user,
#                 activation_key=activation_key,
#                 activation_key_expirity=key_expires)
#             new_user.save()

#             email_subject = 'Your new site account confirmation'
#             email_body = """Hello, %s, Your account is successfully created
#             \n\nTo activate your account, click this link within 48
#              hours:\n\nhttp://rally.co.tz/confirm/%s""" % (
#                 form.cleaned_data['email'],
#                 new_user.activation_key)
#             send_mail(email_subject,
#                       email_body,
#                       'rallytanzaniaemailhost@gmail.com',
#                       [form.cleaned_data['email']])

#             context = {
#                 'code': 200,
#                 'status': ' success',
#                 'error_message': 'Registration successfull',
#                 'error_info': """Your account is not activated yet, we've you sent and email with activation 
#                                   code to activate your account"""
#             }
#             return render(request, 'registration/activate_account.html', context)
#         else:
#             context = {
#                 'code': 404,
#                 'status': 'failed',
#                 'error_message': 'Registration failed',
#                 'error_info': """This error might be because of invalid data on the form, 
#                                   or the user with the same information already exist"""
#             }
#             return render(request, 'registration/activate_account.html', context)
#     else:
#         return render(request, 'registration/guidance.html')


# def activate_account(request):
#     return render(request, 'registration/activate_account.html')


# def confirm_account(request, id):
#     try:
#         user = UserProfile.users.get(activation_key=id)
#     except:
#         context = {
#             'code': 404,
#             'status': 'failed',
#             'error_message': 'Key expired',
#             'error_info': """You are seeing this error because the time to use the activation
#                                   key to activate your account is passed or the key is used, 
#                                   please request for activation new code"""
#         }
#         return render(request, 'registration/activate_account.html', context)

#     if user is not None:
#         if user.activation_key_expirity < timezone.now():
#             context = {
#                 'code': 404,
#                 'status': 'failed',
#                 'error_message': 'Key expired',
#                 'error_info': """You are seeing this error because the time to use the activation
#                                   key to activate your account is passed or the key is used, 
#                                   please request for activation new code"""
#             }
#             return render(request, 'registration/activate_account.html', context)
#         new_user = user.user
#         new_user.is_active = True
#         user.activation_key += random.randint(2, 1000000)
#         new_user.save()
#         user.save()
#         context = {
#             'code': 200,
#             'status': ' success',
#             'error_message': 'Activation successfull',
#             'error_info': """Your account is activated, you can now login and continue with registration"""
#         }
#         return render(request, 'registration/activate_account.html', context)

#     else:
#         context = {
#             'code': 404,
#             'status': 'failed',
#             'error_message': 'This activation is not valid',
#             'error_info': """You are seeing this error because you might be trying to use the key 
#                                   that is already used"""
#         }
#         return render(request, 'registration/activate_account.html', context)


# def reset_password_email(request):
#     fresh_form = forms.PasswordReset()
#     if request.method == 'POST':
#         form = forms.PasswordReset(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = CustomUser.users.get(email=email)
#             except:
#                 user = None

#             if user is not None:
#                 # creating activation key and save it together with the user
#                 # x is to differentiate between keys of unactivated users
#                 x = datetime.datetime.today()
#                 activation_key = random.randint(
#                     1, 1000) + x.year + x.month + x.day + x.hour + x.minute + x.second
#                 key_expires = datetime.datetime.today() + datetime.timedelta(2)

#                 try:
#                     new_user = UserProfile.users.get(user=user)
#                 except:
#                     context = {
#                         'code': 404,
#                         'status': 'failed',
#                         'error_message': 'Key expired',
#                         'error_info': """You are seeing this error because the time to use the link
#                                             for your password reset is expired, repeate the request to get
#                                             the new link"""
#                     }
#                     return render(request, 'registration/activate_account.html', context)
#                 new_user.activation_key = activation_key
#                 new_user.activation_key_expirity = key_expires
#                 new_user.save()

#                 email_subject = 'Password reset confirmation'
#                 email_body = """Hello, %s, Your account password reset request is accepted
#                 \n\nTo reset your password, click this link within 48
#                 hours:\n\nhttp://rally.co.tz/setmynewpassword/?id=%s""" % (
#                     form.cleaned_data['email'],
#                     new_user.activation_key)
#                 send_mail(email_subject,
#                           email_body,
#                           'rallytanzaniaemailhost@gmail.com',
#                           [form.cleaned_data['email']])

#                 context = {
#                     'code': 200,
#                     'status': ' success',
#                     'error_message': 'Request successfull',
#                     'error_info': """Your request is succesfuly sent, please visit your email and click 
#                                       the link we've sent you"""
#                 }
#                 return render(request, 'registration/activate_account.html', context)
#             else:
#                 message = "user with this email does not exist"
#                 template = 'authentication/password_reset.html'
#                 return show_auth_error(request, fresh_form, email, message, template, action=0)
#         else:
#             message = "please, provide a clean password for your account"
#             template = 'authentication/password_reset.html'
#             return show_auth_error(request, fresh_form, "", message, template, action=0)
#     else:
#         return render(request, 'authentication/password_reset.html', {'form': fresh_form, 'action': 0})


# def reset_password(request):
#     try:
#         user = UserProfile.users.get(activation_key=request.GET.get('id'))
#     except:
#         context = {
#             'code': 404,
#             'status': 'failed',
#             'error_message': 'Key expired',
#             'error_info': """You are seeing this error because the time to use the link
#                                   for your password reset is expired, repeate the request to get
#                                   the new link"""
#         }
#         return render(request, 'registration/activate_account.html', context)
#     if user is not None:
#         fresh_form = forms.Newpassword()
#         if user.activation_key_expirity < timezone.now():
#             context = {
#                 'code': 404,
#                 'status': 'failed',
#                 'error_message': 'Key expired',
#                 'error_info': """You are seeing this error because the time to use the activation
#                                   key to activate your account is passed or the key is used, 
#                                   please request for activation new code"""
#             }
#             return render(request, 'registration/activate_account.html', context)
#         new_user = user.user
#         if request.method == 'POST':
#             form = forms.Newpassword(request.POST)
#             if form.is_valid():
#                 new_user.set_password(form.cleaned_data['password2'])
#                 new_user.save()
#                 user.activation_key += random.randint(2, 1000000)
#                 user.save()
#                 context = {
#                     'code': 200,
#                     'status': ' success',
#                     'error_message': 'Password reset successfull',
#                     'error_info': """You can now login to your account with your new passowrd"""
#                 }
#                 return render(request, 'registration/activate_account.html', context)
#             else:
#                 message = "please, provide a clean password for your account"
#                 template = 'authentication/password_reset.html'
#                 return show_auth_error(request, fresh_form, "", message, template, action=0)
#         else:
#             return render(request, 'authentication/password_reset.html', {'form': fresh_form, 'action': 1})
#     else:
#         context = {
#             'code': 404,
#             'status': 'failed',
#             'error_message': 'Key expired',
#             'error_info': """You are seeing this error because the time to use the activation
#                               key to activate your account is passed or the key is used, 
#                               please request for activation new code"""
#         }
#         return render(request, 'registration/activate_account.html', context)


# def iaa_registration(request):
#     if request.user.is_authenticated:
#         iaa_user_registration_form = forms.IaaRegistration()
#         if request.method == 'POST':
#             status = register_user_from_iaa(request.POST)
#             if status == 'success':
#                 return redirect('.')
#             else:
#                 context = {
#                     'is_iaa': True,
#                     'form': iaa_user_registration_form,
#                     'with_error': True,
#                     'error_title': "Failed!!",
#                     'error_info': status,
#                     'registered_users': IaaRegistered.registered_users.all()
#                 }

#                 return render(request, 'registration/iaa.html', context)
#         else:
#             registered_users = IaaRegistered.registered_users.all()

#             context = {

#                 # some users can only have certain menus
#                 # eg:- iaa members
#                 'is_iaa': True,

#                 'form': iaa_user_registration_form,

#                 # if form is not valid show the error at the top
#                 'with_error': False,

#                 'registered_users': registered_users
#             }

#             return render(request, 'registration/iaa.html', context)
#     else:
#         context = {
#             'code': 403,
#             'status': ' Forbiden',
#             'error_message': 'view blocked',
#             'error_info': 'You\'re either not logged in or your session is expired, please login again'
#         }
#         return render(request, 'registration/activate_account.html', context)


# def register_user_from_iaa(form_data):
#     form = forms.IaaRegistration(form_data)
#     if form.is_valid():
#         if form_data['type'] == "driver":
#             try:
#                 door_number = IaaRegistered.registered_users.get(id=form_data['door_number'])
#             except:
#                 door_number = None

#             if door_number is None:
#                 form.save(commit=True)
#                 status = 'success'
#                 return status
#             else:
#                 status = """
#                             invalid data entered or user with the same 
#                             door number/license number already exists,
#                             please check your inputs
#                         """
#                 return status
#         else:
#             form.save(commit=True)
#             status = 'success'
#             return status
            
#     else:
#         status = """
#                     invalid data entered or user with the same 
#                     door number/license number already exists,
#                      please check your inputs
#                 """
#         return status


# def delete_user_from_iaa(request, user_id):
#     if request.method == "GET":
#         iaa_user_registration_form = forms.IaaRegistration()
#         try:
#             IaaRegistered.registered_users.get(pk=user_id).delete()
#         except:
#             context = {
#                 'is_iaa': True,
#                 'form': iaa_user_registration_form,
#                 'with_error': True,
#                 'error_title': "Failed!!",
#                 'error_info': "User not found"
#             }
#             return render(request, 'registration/iaa.html', context)
#         return redirect('../iaa')
#     else:
#         return redirect('../iaa')


# def club_registration(request):
#     registration_form = forms.ClubRegistration()
#     if request.method == "GET":
#         return render(request, 'registration/register.html', {"form": registration_form})


# def driver_navigator_registration(request):

#     if request.method == "GET":
#         return render(request, 'registration/driver_nav_registration.html')


# class ValidateUserFromIAA(APIView):
#     serializer = get_serializer(IaaRegistered, fields=(
#         'first_name', 'last_name', 'license_number', 'door_number', 'type'))

#     def post(self, request, format=None):
#         license_number = request.data['license_number']
#         user = IaaRegistered.registered_users.filter(
#             license_number=license_number)

#         if user is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return serialize_queryset(user, self.serializer)


# class RegisterDriverNavigator(APIView):

#     def post(self, request, format=None):

#         try:
#             iaa_user = IaaRegistered.registered_users.get(
#                 license_number=request.data['license_number'])

#             if iaa_user.is_fully_registered:
#                 return Response(status=status.HTTP_403_FORBIDDEN)
#             else:
#                 if request.data['door_number'] == '-1':
#                     type = 'navigator'
#                     door_number = 'N/A'
#                 else:
#                     type = 'driver'
#                     door_number = request.data['door_number']

#                 user = CustomUser.users.create_user(
#                     email=request.data['email'],
#                     password=request.data['password'],
#                     first_name=request.data['first_name'],
#                     last_name=request.data['last_name']
#                 )
#                 user.is_active = True
#                 if type == 'driver':
#                     user.is_a_driver = True
#                 elif type == 'navigator':
#                     user.is_a_navigator = True
#                 user.save()

#                 driverNavigator = DriverNavigator.users.create(
#                     user=user,
#                     license_number=request.data['license_number'],
#                     type=type,
#                     door_number=door_number
#                 )
#                 driverNavigator.save()
#                 iaa_user.is_fully_registered = True
#                 iaa_user.save()
#                 return Response(status=status.HTTP_200_OK)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# # provides context for driver navigator context
# def context_provider(   
#                 request, 
#                 attachment_error=False, 
#                 global_error=False, 
#                 title=None, 
#                 info=None, 
#                 template=None,
#                 success_status=False
#             ):
#     try:
#         driver_navigator = request.user.drivernavigator
#     except:
#         driver_navigator = None

#     if driver_navigator is not None:
#         attachments = Attachments.attachments.filter(driverNavigator=driver_navigator)
#         profile_picture = driver_navigator.profile_picture
#         images = CarPhotos.images.filter(driverNavigator=driver_navigator)
#     else:
#         attachments = None
#         profile_picture = None
#         images = None

#     context = {
#         'attachments': attachments,
#         'media': settings.MEDIA_URL,
#         'profile_picture': profile_picture,
#         'images': images,
#         'section': 'profile',
#         'forms': {
#             'attachment': forms.AttachmentsForm,
#         },
#         'attachment_error': attachment_error,
#         'global_error': global_error,
#         'success_status': success_status,
#         'title': title,
#         'info': info
#     }
#     return render(request, template, context)


# def show_driver_navigator_profile(request):
#     if request.method == "GET":
#         return context_provider(request, template='profiles/driver_nav.html')


# def post_attachments(request):
#     if request.method == 'POST':
#         form = forms.AttachmentsForm(request.POST, request.FILES)
#         if form.is_valid():
#             attachment = form.save(commit=False)
#             attachment.driverNavigator = request.user.drivernavigator
#             attachment.save()
#             return redirect('../driver_navigator_profile')
#         else:
#             return context_provider(request,
#                                     attachment_error=True,
#                                     title="FAILED TO UPLOAD!!",
#                                     info="this might be due to empty inputs or invalid file",
#                                     template='profiles/driver_nav.html'
#                                     )
#     else:
#         return redirect('../driver_navigator_profile')


# def delete_driver_naivgator_attachment(request, id):
#     if request.method == "GET":
#         try:
#             Attachments.attachments.get(pk=id).delete()
#             return redirect('../driver_navigator_profile')
#         except:
#             return context_provider(request,
#                                     attachment_error=True,
#                                     title="FAILED TO DELETE!!",
#                                     info="""this file might have alerady been deleted, 
#                                     or something went worng with the server""", 
#                                     template='profiles/driver_nav.html')
#     else:
#         return redirect('../driver_navigator_profile')


# def upload_car_photo(request):
#     if request.method == "POST":
#         form = forms.CarPhotosForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.driverNavigator = request.user.drivernavigator
#             image.save()
#             return redirect('../driver_navigator_profile')
#         else:
#             return context_provider(request,
#                                     global_error=True,
#                                     title="COULD NOT UPLOAD PHOTO!!",
#                                     info=""" it might be due to empty inputs or invalid file,
#                                     please try again""",
#                                     template='profiles/driver_nav.html')
#     else:
#         return redirect('../driver_navigator_profile')


# def delete_car_image(request, id):
#     if request.method == "GET":
#         try:
#             CarPhotos.images.get(pk=id).delete()
#             return redirect('../driver_navigator_profile')
#         except:
#             return context_provider(request,
#                                     global_error=True,
#                                     title="COULD NOT DELETE PHOTO!!",
#                                     info=""" this file might have already been deleted, 
#                                     or something went worng with the server""",
#                                     template='profiles/driver_nav.html')
#     else:
#         return redirect('../driver_navigator_profile')

# def request_club_registration(request):
#     if request.method == "GET":
#         form = forms.ClubRequestingForRegistrationForm
#         return render(request, 'registration/clubregistration.html', {'form': form})
#     elif request.method == "POST":
#         form = forms.ClubRequestingForRegistrationForm(request.POST)
#         if form.is_valid():
#             club = form.save(commit=False)

#             # notify the admin for the registration request
#             admin_email = SystemInfo.info.get(system_id=0).email
#             email_subject = 'REQUESTING FOR CLUB REGISTRATION'
#             email_body = """ %s is requesting for club registration """ % (form.cleaned_data['email'])
#             send_mail(email_subject, email_body, 'rallytanzaniaemailhost@gmail.com', [admin_email, ])
#             club.save()

#             return context_provider(request,
#                                     success_status = True,
#                                     title="CLUB REGISTRATION REQUEST SUCCESSFULL!!",
#                                     info=""" 
#                                             you will be notified through your email when your request is processed,
#                                             note that this might take a few hours or days, be patient and thank you
#                                          """,
#                                     template='registration/clubregistration.html')
#         else:
#             return context_provider(request,
#                                     global_error=True,
#                                     title="COULD NOT REQUEST FOR REGISTRATION!!",
#                                     info=""" It might be due to wrong inputs or this email is already used,
#                                              if you think this email or name is already used please contact us with this email
#                                              to verify %s"""%(SystemInfo.info.get(system_id=0).email),
#                                     template='registration/clubregistration.html')
