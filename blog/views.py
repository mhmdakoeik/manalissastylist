from django.shortcuts import render
from .models import Blog
from .utils import paginateBlogs

def blogs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    allBlogs = Blog.objects.filter(title__icontains=search_query).order_by('created')
    custom_range, paginated_blogs = paginateBlogs(request, allBlogs, 1)

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