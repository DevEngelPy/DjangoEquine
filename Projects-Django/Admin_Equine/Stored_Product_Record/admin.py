from typing import Any
from django.contrib import admin
from Stored_Product_Record.models import Product_registration
from django.core.exceptions import ValidationError
# Register your models here.

@admin.register(Product_registration)
class Product_registrationAdmin(admin.ModelAdmin):
    list_display = ('id_supplier','id_produc_shop', 'created','state',)
    fields = (('id_produc_shop','id_supplier'), ('amount','unit'),'price','total','state',)
    readonly_fields = ('total',)
    list_filter = ('created',)
    
        
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
    
        total:float = float(obj.amount) * float(obj.price)
        obj.total = total
        print(f'el total es : {obj.total}')
        
        return super().save_model(request, obj, form, change)
    