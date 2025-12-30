from django.urls import path

from . import views

urlpatterns = [
    path("", views.AuthenticationView.as_view(), name="sign_in"),
    path("sign-out", views.sign_out, name="sign_out"),
    path("auth-receiver", views.auth_receiver, name="auth_receiver"),
]
