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
            'card_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card_CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }


DATE_CHOISES = [(x, str(x)) for x in range(1, 13)]


class PaymentForm2(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        fields = {
            'card_number': CardNumberField(label='Card Number'),
            'card_month': forms.ChoiceField(label='Card month', choices=DATE_CHOISES),
            #'card_year': forms.ChoiceField(choices=[[0, 'Days'], [1, 'Weeks'], [3, 'Months']]),
                #NumberInput(widget=forms.Select(choices=DATE_CHOISES)),
            #'card_month': forms.IntegerField(label='Expiration Date', widget=forms.Select(choices=DATE_CHOISES)),
            #'card_month': CardExpiryField(label='Expiration Date'),
            'card_CVC': SecurityCodeField(label='CVV/CVC')
        }


class PaymentForm3(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_month': widgets.Select(attrs={'class': 'form-control'}),
            'card_year': widgets.Select(attrs={'class': 'form-control'}),
            'card_CVC': widgets.TextInput(attrs={'class': 'form-control'})
        }



#class PaymentForm(forms.Form):
#    cc_number = CardNumberField(label='Card Number')
#    cc_expiry = CardExpiryField(label='Expiration Date')
#    cc_code = SecurityCodeField(label='CVV/CVC')
