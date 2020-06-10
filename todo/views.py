from django.shortcuts import render
from .models import Image


def home(request):
    images = Image.objects.all()
    context = {"images": images}
    return render(request, 'todo/home.html', context)
