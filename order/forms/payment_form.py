from django.forms import ModelForm, widgets
from order.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '16', 'minlength': '16'}),
            'card_month': widgets.Select(attrs={'class': 'form-control'}),
            'card_year': widgets.Select(attrs={'class': 'form-control'}),
            'card_CVC': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '3', 'minlength': '3'})
        }
