from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from home.forms.newsletter_form import NewsletterForm

# Create your views here.
from home.models import Newsletter


def index(request):
    if request.method == 'GET':
        form = NewsletterForm()
    else:
        userform = NewsletterForm(data=request.POST)
        if userform.is_valid():
            userform.save(commit=False)
            userform.save()
            form = NewsletterForm()

    return render(request, 'home/index.html', {
        'form': form
    })

from django.core.validators import validate_email


def add_to_newsletter(request, email):
    if request.method == 'POST':
        if validate_email(email):
            if Newsletter.objects.filter(email__exact=email): # ef er núþegar skráður
                existing_newsletter = Newsletter.objects.get(email__exact=email)
                existing_newsletter.save()
            else:
                Newsletter.objects.create(email=email)


    return render(request, 'home/index.html')


