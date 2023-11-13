from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("dashboard/", include("dashboard.urls")),
    path('verification/', include('verify_email.urls')),
    path("", include("home.urls")),
    path("books/", include("books.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
