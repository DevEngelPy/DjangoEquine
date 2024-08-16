from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.

class Type(models.Model):
    name = models.CharField(_("name"), max_length=20)
    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})
   
class Product_sale(models.Model):

    name = models.CharField(_("name"), max_length=50)
    price = models.FloatField(_("price"), max_length=6)
    type  = models.ForeignKey(Type, verbose_name=_("type"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Product_sale")
        verbose_name_plural = _("Product_sales")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_sale_detail", kwargs={"pk": self.pk})

class Product_purchase(models.Model):

    name = models.CharField(_("name"), max_length=50)
    price = models.FloatField(_("price"), max_length=6)
    type  = models.ForeignKey(Type, verbose_name=_("type"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Product_purchase")
        verbose_name_plural = _("Product_purchases")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_shopProduct_purchase_detail", kwargs={"pk": self.pk})
