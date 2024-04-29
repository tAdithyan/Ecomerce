from django.contrib import admin

# Register your models here.
from .models import Order,OrderedIteam
admin.register(Order)
admin.register(OrderedIteam)