from django.shortcuts import render
from .models import MultiImageModel
from .models import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .utils import paginateGallery


@receiver(pre_delete, sender=Image)
def delete_image_files(sender, instance, **kwargs):
    # Delete the associated image file when an Image instance is deleted
    instance.image.delete(save=False)

def image_gallery(request):
    try:
        multi_images = Image.objects.all()
        custom_range, paginated_gallery = paginateGallery(request, multi_images, 8)
        context = {'multi_images': paginated_gallery, 'custom_range': custom_range}
    except Image.DoesNotExist:
        multi_images = None
        context = {'multi_images': multi_images}
    return render(request, 'gallery/image_gallery.html', context)
