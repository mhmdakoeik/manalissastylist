from django.shortcuts import render
from .models import Slider,WhyChooseOurServices,Gallery
# Create your views here.
def home(request):
    slider = Slider.objects.all()
    whyUs = WhyChooseOurServices.objects.all()
    gallery = Gallery.objects.all()
    context = {'slider':slider,'whyUs':whyUs,'gallery':gallery}
    return render(request, "home/index.html",context) 