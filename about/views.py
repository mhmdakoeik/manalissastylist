from django.shortcuts import render
from .models import About
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=About)
def delete_or_update_image_files_about(sender, instance, **kwargs):
    if instance.pk:
        old_instance = About.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            old_instance.image.delete(save=False)

def about(request):
    aboutObj = About.objects.all()
    context = {'about': aboutObj}
    return render(request, 'about/about.html', context)