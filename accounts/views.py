from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
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
