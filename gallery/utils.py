from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def paginateGallery(request,gallery,results):
    page = request.GET.get('page')
    paginator = Paginator(gallery,results)

    try:    
        gallery = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        gallery = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        gallery = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex,rightIndex)
    return custom_range,gallery