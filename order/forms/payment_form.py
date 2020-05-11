from django.forms import ModelForm, widgets
from order.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card_CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }

