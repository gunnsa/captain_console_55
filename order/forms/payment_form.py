from django.forms import ModelForm, widgets
from order.models import Payment
from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card_month': widgets.DateInput(attrs={'class': 'form-control'}),
            'card_year': widgets.DateInput(attrs={'class': 'form-control'}),
            'card_CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class PaymentForm2(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')
