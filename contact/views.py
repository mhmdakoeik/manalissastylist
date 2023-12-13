from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender_email = form.cleaned_data['email']
            sender_name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = f"From: {sender_name}\n\nEmail: {sender_email}\n\n {form.cleaned_data['message']}"

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
