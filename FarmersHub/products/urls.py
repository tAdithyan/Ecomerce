
from . import views





from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='index'),
    path('products/', views.products, name='products'),
    path('productsdetails/<pk>', views.product_details, name='product_details'),
    path('Cart/', views.cart, name='cart'),
    path('Account/', views.Account, name='Account'),



]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
