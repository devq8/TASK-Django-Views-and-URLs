from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def get_product(request, product_id):
    # all_products = Product.objects.all()
    product = Product.objects.get(id=product_id)
    product_massage = ("<p>The selected product details are below</p>\n"
        f"\n <p>The product id is : {product.id}</p>"
        f"\n <p>The product name is : {product.name}</p>")


    return HttpResponse(f"<h1>{product_massage}</h1>")