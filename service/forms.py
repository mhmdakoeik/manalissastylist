from django.forms import ModelForm,Textarea
from .models import Feedback

class FeedbackForm(ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['avatar','name','email','message']

        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 10}),
        }