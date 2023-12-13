from .models import Service
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def paginateServices(request,services,results):
    page = request.GET.get('page')
    paginator = Paginator(services,results)

    try:    
        services = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        services = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        services = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex,rightIndex)
    return custom_range,services