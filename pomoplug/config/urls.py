"""
URL configuration for tomacheck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from authentication.views import AuthenticationView
from django.contrib import admin
from django.urls import include, path
from timer.views import TimerCreateView, TimerView, HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", AuthenticationView.as_view(), name="authentication-view"),
    path("timer/new", TimerCreateView.as_view(), name="timer-create"),
    path("timer/<str:uuid>", TimerView.as_view(), name="timer-view"),
    path("auth/", include("authentication.urls")),
    path("", HomeView.as_view(), name="home-view")
]
