from django.shortcuts import render
from .models import Slider,WhyChooseOurServices,Gallery

from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=Slider)
def delete_or_update_image_files_about(sender, instance, **kwargs):
    try:
        old_instance = Slider.objects.get(pk=instance.pk)
    except Slider.DoesNotExist:
        return  # Handle the case where the instance doesn't exist

    if old_instance.image != instance.image:
        old_instance.image.delete(save=False)

@receiver([pre_delete, pre_save], sender=WhyChooseOurServices)
def handle_whychoose_icon_files(sender, instance, **kwargs):
    if not instance.pk:
        return  # If it's a new instance, there's nothing to do
    try:
        old_instance = WhyChooseOurServices.objects.get(pk=instance.pk)
    except WhyChooseOurServices.DoesNotExist:
        return  # If the instance does not exist, exit the function
    # Loop through each icon field and delete the old file if it has been updated
    for i in range(1, 5):
        field_name = f'icon_{i}'
        old_icon = getattr(old_instance, field_name)
        new_icon = getattr(instance, field_name)
        if old_icon and old_icon != new_icon:
            old_icon.delete(save=False)  # Delete the old icon file

@receiver([pre_delete, pre_save], sender=Gallery)
def handle_image_files(sender, instance, **kwargs):
    if not instance.pk:
        return  # If it's a new instance, there's nothing to do
    try:
        old_instance = Gallery.objects.get(pk=instance.pk)
    except Gallery.DoesNotExist:
        return  # If the instance does not exist, exit the function
    # Loop through each icon field and delete the old file if it has been updated
    for i in range(1, 4):
        field_name = f'image_{i}'
        old_image = getattr(old_instance, field_name)
        new_image = getattr(instance, field_name)
        if old_image and old_image != new_image:
            old_image.delete(save=False)  # Delete the old icon file

def home(request):
    slider = Slider.objects.all()
    whyUs = WhyChooseOurServices.objects.all()
    gallery = Gallery.objects.all()
    context = {'slider':slider,'whyUs':whyUs,'gallery':gallery}
    return render(request, "home/index.html",context) 