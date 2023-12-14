from django.shortcuts import render
from .models import Service,Feedback
from .utils import paginateServices
from .forms import FeedbackForm

def services(request):
    all_services = Service.objects.all().order_by('created')
    custom_range, paginated_services = paginateServices(request, all_services, 3)
    context = {'services': paginated_services, 'custom_range': custom_range}
    return render(request, 'services/services.html', context)

def service(request,pk):
    service = Service.objects.get(id=pk)
    context = {'service':service}
    return render(request,'services/service.html',context)

def feedbacks(request):
    feedbacks = Feedback.objects.filter(show=True).values()
    context = {'feedbacks':feedbacks}
    return render(request,context)


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    
    info_form = form.visible_fields()[:3] if hasattr(form, 'visible_fields') else []
    feedback_form = form.visible_fields()[3:] if hasattr(form, 'visible_fields') else []
    context = {'feedback_form': feedback_form, 'info_form': info_form}
    return render(request, 'services/feedback_form.html', context)
