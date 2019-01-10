"""CameraFeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Feed import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login



urlpatterns = [
    path('', views.camerafeed, name="camerafeed"),
    path("next=/camerafeed/", views.camerafeed),
    path('admin/', admin.site.urls),
    path('camerafeed/', include('Feed.urls')),
    path("logout/", logout_then_login, name="logout"),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html')),
    path('accounts/login/camerafeed/', views.camerafeed),
]


