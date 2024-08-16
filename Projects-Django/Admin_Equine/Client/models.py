from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Client(models.Model):

    name = models.CharField(_("name"), max_length=30)
    account_status = models.FloatField(_("account status"), default=0)
    abono = models.FloatField(_("abono"), default=0, validators=[MinValueValidator(0)])
    status = models.BooleanField(_("status"), default=False)
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    update = models.DateTimeField(_("update"), auto_now=True, auto_now_add=False)
    
    
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})
