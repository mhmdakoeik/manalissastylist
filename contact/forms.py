from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        self.fields['message'].initial = '' 
        self.fields['name'].initial = '' 
        self.fields['email'].initial = '' 
        self.fields['subject'].initial = '' 

 
