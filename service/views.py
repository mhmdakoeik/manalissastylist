from django.shortcuts import render
from .models import Service
from .utils import paginateServices

def services(request):
    all_services = Service.objects.all().order_by('created')
    custom_range, paginated_services = paginateServices(request, all_services, 3)
    context = {'services': paginated_services, 'custom_range': custom_range}
    return render(request, 'services/services.html', context)

def service(request,pk):
    service = Service.objects.get(id=pk)
    context = {'service':service}
    return render(request,'services/service.html',context)
