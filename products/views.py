from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def get_product(request, product_id):
    product_massage = ("The selected product id is : \n"
        f"\n {product_id}")


    return HttpResponse(f"<h1>{product_massage}</h1>")