from django.shortcuts import redirect, render
from .models import Service,Feedback
from .utils import paginateServices
from .forms import FeedbackForm
from django.dispatch import receiver
from django.db.models.signals import pre_delete,pre_save
import uuid


@receiver([pre_delete, pre_save], sender=Feedback)
def delete_image_files_feedback(sender, instance, **kwargs):
    instance.avatar.delete(save=False)

@receiver([pre_delete, pre_save], sender=Service)
def delete_or_update_image_files_service(sender, instance, **kwargs):
    if instance.pk:  # Check if instance exists (i.e., being updated)
        try:
            old_instance = Service.objects.get(pk=instance.pk)
            
            if old_instance.main_image != instance.main_image:
                old_instance.main_image.delete(save=False)
            
            if old_instance.image_1 != instance.image_1:
                old_instance.image_1.delete(save=False)
        
        except Service.DoesNotExist:
            pass  # Handle the case where the instance doesn't exist

    else:  # Instance is being deleted
        if instance.main_image:
            instance.main_image.delete(save=False)
        
        if instance.image_1:
            instance.image_1.delete(save=False)

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

