from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}))
    phone_number = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره همراه'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password1', _("The two password fields didn’t match."))

        username = cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            self.add_error('username', _("A user with that username already exists"))

        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error('email', _("An account with this email address already exists"))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        validate_password(password)
        return password

    def save(self, commit=True):
        User = get_user_model()
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            is_active=not commit  # Set user as inactive if commit is False
        )
        return user


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'input'})
        self.fields['new_password1'].widget.attrs.update({'class': 'input'})
        self.fields['new_password2'].widget.attrs.update({'class': 'input'})
