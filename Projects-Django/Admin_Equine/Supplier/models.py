from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Supplier(models.Model):

    name = models.CharField(_("name"), max_length=50)
    cell = models.IntegerField(_("cell"))
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Supplier_detail", kwargs={"pk": self.pk})
