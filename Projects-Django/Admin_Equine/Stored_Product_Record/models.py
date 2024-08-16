from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from Products.models import Product_purchase 
from Supplier.models import Supplier
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Product_registration(models.Model):

    class Choice_unit(models.TextChoices):
        KG  = 'KG',_('kilogramo')
        PZ = 'PZ',_('pieza')

    id_produc_shop = models.ForeignKey(Product_purchase, verbose_name=_("product"), on_delete=models.CASCADE)
    id_supplier = models.ForeignKey(Supplier, verbose_name=_("supplier"), on_delete=models.CASCADE)
    amount = models.FloatField(_("amount"),max_length=7, validators=[MinValueValidator(0)])
    unit = models.CharField(_("unit"), max_length=2, choices=Choice_unit.choices, default=Choice_unit.KG)
    price = models.FloatField(_("price"), max_length=4, validators=[MinValueValidator(0)])
    total = models.FloatField(_("total"), max_length=6, blank=True)
    state = models.BooleanField(_("state"), default=False)
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    update = models.DateTimeField(_("update"), auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name = _("Product_registration")
        verbose_name_plural = _("Product_registrations")

    def __str__(self):
        return self.id_produc_shop.name
    #validacion
    def clean(self) -> None:
        if self.amount < 0:
            raise ValidationError('no es amitido')
        if self.price < 0:
            raise ValidationError('no es amitido')
    
    def get_absolute_url(self):
        return reverse("Product_registration_detail", kwargs={"pk": self.pk})
