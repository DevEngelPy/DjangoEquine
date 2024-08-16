from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from Client.models import Client
from Products.models import Product_sale

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Note(models.Model):

    id_client = models.ForeignKey(Client, verbose_name=_("Client"), on_delete=models.CASCADE)
    id_product_sale = models.ForeignKey(Product_sale, verbose_name=_("Product sale"), on_delete=models.CASCADE)
    amount = models.FloatField(_("amount"), max_length=6, default=0, validators=[MinValueValidator(0)])
    previous_credit = models.FloatField(_("previous credit"), max_length=6, default=0)
    total = models.FloatField(_("total"),max_length=6, default=0)
    account_credit = models.FloatField(_("account credit"), blank=True, default=0)
    status = models.BooleanField(_("status"), default=False)
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    update = models.DateTimeField(_("update"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def __str__(self):
        return self.id_client.name

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})
