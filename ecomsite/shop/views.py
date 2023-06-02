from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def index(request):
    products_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    #Search code:
    if item_name and item_name is not None:
        products_objects = products_objects.filter(title__contains=item_name)

    # Pagintator Code:
    pagintator = Paginator(products_objects, 4)
    page = request.GET.get('page')
    print("page is: ", page)
    products_objects = pagintator.get_page(page)

    return render(request,'shop/index.html', {'products_objects': products_objects})

def detail(request, id):
     products_object = Products.objects.get(id=id)
     print(products_object.catgory)
     return render(request,'shop/detail.html', {'products_object': products_object})

class CheckoutApi(APIView):
    def get(self, request):
        return render(request, 'shop/checkout.html')
    def post(self, request):
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        total = request.POST.get('total', '')
        order = Order(name=name, email=email, city=city, address=address, items=items, total=total)
        order.save()
        return redirect('/')
