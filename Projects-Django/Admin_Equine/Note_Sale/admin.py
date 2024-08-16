from typing import Any
from django.contrib import admin
from Note_Sale.models import Note
from Client.models import Client
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id_client','id_product_sale','previous_credit','account_credit','created',)
    fields = (('id_client','id_product_sale'),'amount','total',)
    readonly_fields = ('total',)
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        
        #estado de la cuenta del cliente deuda anterior
        obj.previous_credit = obj.id_client.account_status#consulto el saldo
        anterior = obj.previous_credit#introdusco el valor al campo
        #calculo del total
        price = obj.id_product_sale.price
        amount = obj.amount
        total = float(price)*float(amount) + float(anterior)
        obj.total = total 
        obj.account_credit = total
        #actualizar y guardar el valor en el modelo de cliente
        get_client = Client.objects.get(name = obj.id_client)
        get_client.account_status = total
        if get_client != 0.0:
            get_client.status = False
        get_client.save()
          
        return super().save_model(request, obj, form, change)
  