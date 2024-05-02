from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
  return render(request,'home/index.html')

def products(request):
  product_list=product.objects.all()
  context={
    'products': product_list }
  return render(request,'products/products.html',context)

def product_details(request):
  return render(request,'products/product_details.html')


def cart(request):
  return render(request,'carts/cart.html')


def Account(request):
  return render(request,'account/account.html')