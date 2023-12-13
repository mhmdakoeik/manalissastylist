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
            message = f"From: {sender_email}\n\n{form.cleaned_data['message']}"

            send_mail(
                form.cleaned_data['subject'],
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Message not sent!')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
