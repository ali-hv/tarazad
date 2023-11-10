from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse


def email_verified_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and not user.email_verified:
            # Redirect to a page indicating that email is not verified
            return redirect(reverse('accounts:not_verified', args=['email']))
            # Alternatively, you can return an HttpResponse with a message
            # return HttpResponse("Your email is not verified.")
        return view_func(request, *args, **kwargs)
    return wrapper


def identity_verified_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and not user.identity_verified:
            # Redirect to a page indicating that email is not verified
            return redirect(reverse('accounts:not_verified', args=['identity']))
            # Alternatively, you can return an HttpResponse with a message
            # return HttpResponse("Your email is not verified.")
        return view_func(request, *args, **kwargs)
    return wrapper
