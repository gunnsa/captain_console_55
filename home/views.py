from django.shortcuts import render
from home.models import Newsletter
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def index(request):
    """ Returns view of homepage """
    return render(request, 'home/index.html')


def add_to_newsletter(request, email):
    """ Adds given email to newsletter model in the database """
    if request.method == 'POST':
        print(email)
        print('1')
        print(validate_email(email))
        if validate_email(email):

            if Newsletter.objects.filter(email__exact=email):
                print('2')
                existing_newsletter = Newsletter.objects.get(email__exact=email)
                existing_newsletter.save()
            else:
                Newsletter.objects.create(email=email)
                print('3')
        else:
            print('not valid')

    return render(request, 'home/index.html')
