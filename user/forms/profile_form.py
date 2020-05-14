from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email_address': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '7', 'minlength': '7'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a link to your image...'})
        }
