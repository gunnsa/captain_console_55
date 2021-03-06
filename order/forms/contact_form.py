from django.forms import ModelForm, widgets
from order.models import ContactInformation
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email_address': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '7', 'minlength': '7'}),
            'home_address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '3', 'minlength': '3'}),
            'additional_info': widgets.TextInput(attrs={'class': 'form-control'})
        }
