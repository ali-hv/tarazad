from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_page, name="register"),
    path("change-info/", views.change_info, name="change_info"),
    path("change-password/", views.ChangePassword.as_view(), name="change_password"),
]
