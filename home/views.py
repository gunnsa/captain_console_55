from django.http import HttpResponse
from django.shortcuts import render
from home.forms.newsletter_form import NewsletterForm

# Create your views here.


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
