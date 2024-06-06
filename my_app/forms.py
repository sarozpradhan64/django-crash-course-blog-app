from django import forms 
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        # fields = ['full_name', 'email', 'mobile', 'message']