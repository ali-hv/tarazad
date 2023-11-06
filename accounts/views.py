from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username_input = login_form.cleaned_data.get('username')
            password_input = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')
            else:
                login_form.add_error('password', 'نام کاربری یا رمز عبور صحیح نیستند')
    context = {'login_form': login_form}
    return render(request, 'accounts/login.html', context)