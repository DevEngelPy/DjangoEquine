from typing import Any
from django.contrib import admin
from Products.models import Product_sale,Product_purchase,Type

# Register your models here.

@admin.register(Product_purchase)
class Product_purchaseAdmin(admin.ModelAdmin):
    list_display = ('name','price',)

@admin.register(Product_sale)
class Product_saleAdmin(admin.ModelAdmin):
    list_display = ('name','type','price',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


