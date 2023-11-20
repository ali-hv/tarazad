from verify_email.email_handler import send_verification_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import UserLoginForm, UserRegisterForm
from .scripts.translate_errors import to_persian
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
import threading


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')

    login_form = UserLoginForm()
    form_error = None
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username_input = login_form.cleaned_data.get('username')
            password_input = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')

            form_error = 'نام کاربری یا رمز عبور صحیح نیستند'

    context = {'login_form': login_form, 'error': form_error}
    return render(request, 'accounts/login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            thread = threading.Thread(target=send_verification_email, args=(request, form))
            thread.start()
            
            messages.success(request, "لینک تایید به ایمیل شما ارسال شد. لطفا به ایمیل خود مراجعه و روی لینک کلیک کنید تا اکانت شما فعال شود")
            return redirect('home:home_page')
    else:
        form = UserRegisterForm()

    form_errors = to_persian(form)
    context = {'register_form': form, 'register_form_errors': form_errors}
    return render(request, 'accounts/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home:home_page')


class ChangePassword(PasswordChangeView):
    template_name = 'dashboard/profile.html'  # Customize this with your template
    success_url = reverse_lazy('dashboard:profile')  # Redirect to the user's profile page after a successful password change

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'رمز عبور شما با موفقیت تغییر کرد !')
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = to_persian(form)
        form.error_messages = errors
        messages.error(self.request, 'تغییر رمز عبور با خطا مواجه شد')
        return super().form_invalid(form)


@login_required
def change_info(request):
    if request.method == "POST":
        user = request.user

        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')

        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            user.avatar = avatar

        user.save()

        return JsonResponse({'success': True})

    return redirect('dashboard:profile')


def identity_not_verified(request):
    return render(request, 'accounts/identity_not_verified.html')
