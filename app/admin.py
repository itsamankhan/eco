from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'locality', 'city', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'brand']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'status']

