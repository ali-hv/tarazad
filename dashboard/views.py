from django.http import Http404
from django.shortcuts import render


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    raise Http404
