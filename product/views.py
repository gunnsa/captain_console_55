from django.shortcuts import render, get_object_or_404
from product.models import Product

# Create your views here.
def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)

#/products/id
def get_product_by_id(request, id):
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

def sort_product_by_specific(request, manufacturer):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)


