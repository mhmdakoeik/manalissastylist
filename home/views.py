from django.shortcuts import render
from .models import Slider,WhyChooseOurServices,Gallery

from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=Slider)
def delete_or_update_image_files_slider(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Slider.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            old_instance.image.delete(save=False)

@receiver([pre_delete, pre_save], sender=WhyChooseOurServices)
def delete_or_update_image_files_why(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Slider.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            old_instance.image.delete(save=False)

@receiver([pre_delete, pre_save], sender=WhyChooseOurServices)
def handle_icon_files(sender, instance, **kwargs):
    if instance.pk:  # Check if instance exists (i.e., being updated)
        old_instance = WhyChooseOurServices.objects.get(pk=instance.pk)
        for i in range(1, 5):  # Assuming icons are from icon_1 to icon_4
            field_name = f'icon_{i}'
            old_icon = getattr(old_instance, field_name)
            new_icon = getattr(instance, field_name)
            
            if old_icon and old_icon != new_icon:
                old_icon.delete(save=False)  # Delete old file if updated

    else:  # Instance is being deleted
        for i in range(1, 5):
            field_name = f'icon_{i}'
            icon = getattr(instance, field_name)
            if icon:
                icon.delete(save=False)  # Delete associated files when instance is deleted

@receiver([pre_delete, pre_save], sender=Gallery)
def handle_image_files(sender, instance, **kwargs):
    if instance.pk:  # Check if instance exists (i.e., being updated)
        old_instance = Gallery.objects.get(pk=instance.pk)
        for i in range(1, 6):  # Assuming images are from image_1 to image_5
            field_name = f'image_{i}'
            old_image = getattr(old_instance, field_name)
            new_image = getattr(instance, field_name)
            
            if old_image and old_image != new_image:
                old_image.delete(save=False)  # Delete old file if updated

    else:  # Instance is being deleted
        for i in range(1, 6):
            field_name = f'image_{i}'
            image = getattr(instance, field_name)
            if image:
                image.delete(save=False)  # Delete associated files when instance is deleted

def home(request):
    slider = Slider.objects.all()
    whyUs = WhyChooseOurServices.objects.all()
    gallery = Gallery.objects.all()
    context = {'slider':slider,'whyUs':whyUs,'gallery':gallery}
    return render(request, "home/index.html",context) 