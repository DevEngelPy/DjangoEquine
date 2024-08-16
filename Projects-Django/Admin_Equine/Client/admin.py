from typing import Any
from django.contrib import admin
from Client.models import Client

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','account_status','status',)
    fields = ('name',('account_status','abono'),'status',)
    readonly_fields = ('account_status',)
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        #se descuneta a la cuenta actual 
        abono_a_cuenta = float(obj.account_status) - float(obj.abono)
        obj.account_status = abono_a_cuenta
        obj.abono  = 0.0
        
        return super().save_model(request, obj, form, change)