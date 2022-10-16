from math import prod
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def get_product(request, product_id):
    # all_products = Product.objects.all()
    product = Product.objects.get(id=product_id)




    # Convert object to dictionary.
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price
        }
    }

    return render(request, "product-details.html", context)

def get_products(request):
    all_products = Product.objects.all()

    new_products = []
    for product in all_products:
        new_products.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })


    context = {"products": new_products}

    return render(request, "product-list.html", context)