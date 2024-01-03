from django import forms
from .models import NewsLetter

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(NewsLetterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control input-lg', 'placeholder': 'Your email address'})
        self.fields['email'].initial = ''