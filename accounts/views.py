from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
from .scripts.translate_errors import to_persian


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
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home_page')
    else:
        form = UserRegisterForm()

    form_errors = to_persian(form)
    context = {'register_form': form, 'register_form_errors': form_errors}
    return render(request, 'accounts/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home:home_page')


# views.py
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages


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


def change_info(request):
    if request.user.is_authenticated:
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

    raise Http404

