from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
  return render(request,'home/index.html')

def products(request):
  page=1
  if request.GET:
     page=request.GET.get('page')
  product_list=product.objects.all()
  product_paginator=Paginator(product_list,2)
  product_list=product_paginator.get_page(page)
  context={
    'products': product_list }
  return render(request,'products/products.html',context)

def product_details(request,pk):
  Product=product.objects.get(pk=pk)
  context={
    'product':Product
  }
  return render(request,'products/product_details.html',context)


def cart(request):
  return render(request,'carts/cart.html')


def Account(request):
  return render(request,'account/account.html')