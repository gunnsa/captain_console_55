from django.forms import ModelForm, widgets
from order.models import Delivery


class ProfileForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email_address': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'home_address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'additional_info': widgets.TextInput(attrs={'class': 'form-control'})
        }