from typing import Any
from django.contrib import admin
from Kitchen.models import Cooked_equino

# Register your models here.

@admin.register(Cooked_equino)
class Cooked_equinoAdmin(admin.ModelAdmin):
    list_display = ('product','product_cooked','created',)
    fields = (('product','estimated_shrink'),'product_raw',('product_cooked', 'status'), 'observations',)
    readonly_fields = ('product_cooked',)
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        #calculo
        porsentaje = float(obj.product_raw) * float(obj.estimated_shrink) 
        merma = float(obj.product_raw) - float(porsentaje)
        #asignando resultado
        obj.product_cooked = merma
        
        return super().save_model(request, obj, form, change)
