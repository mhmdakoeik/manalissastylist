from .models import About

def about_processor(request):
    about = About.objects.all()  # Fetch all feedback, you can filter as needed
    return {'about': about}

