from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Cooked_equino(models.Model):

    class Choice_product(models.TextChoices):
        TRE = 'TRE',_('Tripa Equino')
    
    class Choice_merma(models.TextChoices):
        CU = .40,_('40%')
    
    product = models.CharField(_("product"), max_length=3, choices=Choice_product.choices, default=Choice_product.TRE)
    estimated_shrink = models.CharField(_("shrink"), max_length=3, choices=Choice_merma.choices, default=Choice_merma.CU)
    product_raw = models.FloatField(_("product raw"), max_length=5, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    product_cooked = models.FloatField(_("expected loss of knowledge"), max_length=5, blank=True)
    observations = models.TextField(_("observations"), blank=True)
    status = models.BooleanField(_("correct"), default=False)
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    update = models.DateTimeField(_("update"), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = _("Cooked_equino")
        verbose_name_plural = _("Cooked_equinos")

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse("Cooked_equino_detail", kwargs={"pk": self.pk})
