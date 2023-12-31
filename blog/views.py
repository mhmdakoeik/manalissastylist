from django.shortcuts import render
from .models import Blog
from .utils import paginateBlogs
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=Blog)
def delete_or_update_image_files(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Blog.objects.get(pk=instance.pk)
        except Blog.DoesNotExist:
            # This is a new instance, so there's no old instance to compare with
            return

        if old_instance.image != instance.image:
            old_instance.image.delete(save=False)


def blogs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    allBlogs = Blog.objects.filter(title__icontains=search_query).order_by('created')

    # Process each blog to ensure there is an image file before trying to access it
    for blog in allBlogs:
        if not blog.image or not blog.image.file:
            # Handle the case where the image is not present
            # For example, set to None or provide a default image path
            blog.image = None

    custom_range, paginated_blogs = paginateBlogs(request, allBlogs, 2)

    context = {
        'blogs': paginated_blogs,
        'custom_range': custom_range,
        'search_query': search_query
    }
    return render(request, 'blog/blog.html', context)



def blog(request,pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog':blog}
    return render(request,'blog/blog_details.html',context)