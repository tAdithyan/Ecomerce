from django.db import models
from customers.models import Customer
from products.models import product
# Create your models here.
class Order(models.Model):
  LIVE=1
  DELETE=0
  DELETE_CHOICES=((LIVE,'Live'),(DELETE, 'Delete'))
  CART_STAGE=0
  ORDER_CONFIRMED=1
  ORDER_REJECTED=4
  ORDER__PROCESED=2
  ORDER_DELIVERED=3
  STATUS_CHOICE=((ORDER__PROCESED,"ORDER__PROCESED"),
                 (ORDER__PROCESED,"ORDER__PROCESED"),
                 (ORDER_REJECTED,"ORDER_REJECTED"))
  order_Status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
  owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders')
  delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
class OrderedIteam(models.Model):
    procuct=models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="added_iteams")
