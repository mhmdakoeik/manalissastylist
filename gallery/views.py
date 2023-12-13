from django.shortcuts import render
from .models import MultiImageModel
from .models import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Image)
def delete_image_files(sender, instance, **kwargs):
    # Delete the associated image file when an Image instance is deleted
    instance.image.delete(save=False)

def image_gallery(request):
    try:
        multi_image = MultiImageModel.objects.first()
    except MultiImageModel.DoesNotExist:
        multi_image = None
    return render(request, 'gallery/image_gallery.html', {'multi_image': multi_image})
