from .models import Feedback

def feedback_processor(request):
    feedback = Feedback.objects.all()  # Fetch all feedback, you can filter as needed
    return {'feedback': feedback}
