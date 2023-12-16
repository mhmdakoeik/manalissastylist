from django.shortcuts import render
from .models import Blog
from .utils import paginateBlogs
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

@receiver([pre_delete, pre_save], sender=Blog)
def delete_or_update_image_files(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Blog.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            old_instance.image.delete(save=False)

def blogs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    allBlogs = Blog.objects.filter(title__icontains=search_query).order_by('created')
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