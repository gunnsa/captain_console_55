from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def test_cookie(request):
    if not request.COOKIES.get('name'):
        response = HttpResponse("Visiting for the first time.")
        response.set_cookie('name', 'name')
        return response
    else:
        return HttpResponse("Your favorite team is {}".format(request.COOKIES['name']))
