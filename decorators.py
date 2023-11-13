from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse


def identity_verified_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and not user.identity_verified:
            # Redirect to a page indicating that identity is not verified
            return redirect(reverse('accounts:not_verified', args=['identity']))
        return view_func(request, *args, **kwargs)
    return wrapper
