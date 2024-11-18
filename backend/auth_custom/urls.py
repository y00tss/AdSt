from django.urls import path
from django.urls.conf import include
from auth_custom import views as auth_views

urlpatterns = [
    path("register/", auth_views.RegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("profile/", auth_views.ProfileView.as_view(), name="profile"),
]