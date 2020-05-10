from django.forms import ModelForm, widgets
from order.models import ContactInformation


class PaymentForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'user', 'current']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email_address': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'home_address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'delivery_checkbox': widgets.CheckboxInput(attrs={'class': 'form-control'}),
            'additional_info': widgets.TextInput(attrs={'class': 'form-control'})
        }