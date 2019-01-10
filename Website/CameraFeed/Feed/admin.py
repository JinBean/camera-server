from django.contrib import admin
from .models import Feed
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Register your models here.

#admin.site.site_header = 'CameraFeed Dashboard'
admin.site.register(Feed)
admin.site.unregister(Group)


