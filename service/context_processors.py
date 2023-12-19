from .models import Feedback,Service

def feedback_processor(request):
    feedback = Feedback.objects.filter(show=True)
    return {'feedback': feedback}

def service_processor(request):
    service = Service.objects.all()[:3]
    return {'service_f':service}
