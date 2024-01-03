from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import NewsLetterForm

def newsletter_processor(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsLetterForm()

    return {'form': form}
