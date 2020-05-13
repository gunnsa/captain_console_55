from django.forms import ModelForm, widgets

from home.models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        exclude = ['id']
        widgets = {
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here...'})
        }
