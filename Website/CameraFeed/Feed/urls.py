from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.camerafeed, name="camerafeed"),
    path('admin/', admin.site.urls),
    path('camerafeed/', views.camerafeed),
    path('accounts/login/camerafeed/', views.camerafeed),
    path("location1/", views.location1, name="location1"),
    path("location2/", views.location2, name="location2"),


]


