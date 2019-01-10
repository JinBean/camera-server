from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage as storage
import os
from PIL import Image, ImageDraw
import datetime
from io import StringIO
import base64


@login_required()
def camerafeed(request):
    return render(request, 'feedtemplate/feed1.html')

@login_required()
def location1(request):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    seconds = int(now[-2::])
    minutes = int(now[3:5])
    return render(request, 'feedtemplate/Location1.html', {"seconds": seconds, "minutes": minutes, "now": now})

@login_required()
def location2(request):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    seconds = int(now[-2::])
    minutes = int(now[3:5])
    return render(request, 'feedtemplate/Location2.html')



