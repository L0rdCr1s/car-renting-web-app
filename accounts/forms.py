from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = CustomUser.users.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class PasswordReset(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('email',)


class Newpassword(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ()

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class IaaRegistration(forms.ModelForm):

    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    license_number = forms.CharField(max_length=50)
    door_number = forms.IntegerField()

    class Meta:
        model = IaaRegistered
        fields = ('first_name', 'last_name', 'type',
                  'license_number', 'door_number')


class ClubRegistration(forms.ModelForm):

    name = forms.CharField()
    logo = forms.ImageField()
    cover_photo = forms.ImageField()
    description = forms.Textarea()

    class Meta:
        model = Club
        fields = ('user', 'logo', 'cover_photo', 'description', )


class AttachmentsForm(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ('name', 'file', )


class CarPhotosForm(forms.ModelForm):
    class Meta:
        model = CarPhotos
        fields = ('image', )


class ClubRequestingForRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClubRequestingForRegistration
        fields = ('name', 'email', 'password', )
