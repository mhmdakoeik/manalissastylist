from django.shortcuts import render
from .models import About

def about(request):
    aboutObj = About.objects.all()
    context = {'about': aboutObj}
    return render(request, 'about/about.html', context)