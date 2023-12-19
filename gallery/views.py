from django.shortcuts import render
from .models import MultiImageModel
from .models import Image
from .utils import paginateGallery
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=Image)
def delete_or_update_image_files_about(sender, instance, **kwargs):
    try:
        old_instance = Image.objects.get(pk=instance.pk)
    except Image.DoesNotExist:
        return  # Handle the case where the instance doesn't exist
    if old_instance.image != instance.image:
        old_instance.image.delete(save=False)

def image_gallery(request):
    try:
        multi_images = Image.objects.all()
        custom_range, paginated_gallery = paginateGallery(request, multi_images, 8)
        context = {'multi_images': paginated_gallery, 'custom_range': custom_range}
    except Image.DoesNotExist:
        multi_images = None
        context = {'multi_images': multi_images}
    return render(request, 'gallery/image_gallery.html', context)
