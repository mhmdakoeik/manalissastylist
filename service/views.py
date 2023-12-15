from django.shortcuts import redirect, render
from .models import Service,Feedback
from .utils import paginateServices
from .forms import FeedbackForm
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import uuid


@receiver(pre_delete, sender=Feedback)
def delete_image_files(sender, instance, **kwargs):
    instance.avatar.delete(save=False)

def services(request):
    all_services = Service.objects.all().order_by('created')
    custom_range, paginated_services = paginateServices(request, all_services, 3)
    context = {'services': paginated_services, 'custom_range': custom_range}
    return render(request, 'services/services.html', context)

def service(request,pk):
    service = Service.objects.get(id=pk)
    context = {'service':service}
    return render(request,'services/service.html',context)

def feedback_form(request):
    success = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            request.session['form_submitted'] = str(uuid.uuid4())  
            return redirect('feedback')
    else:
        form = FeedbackForm()
    if 'form_submitted' in request.session:
        success = True
        del request.session['form_submitted']
    context = {'form': form, 'success': success}
    return render(request, 'services/feedback_form.html', context)

