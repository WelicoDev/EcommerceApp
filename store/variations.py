from django.db import models
from .manager.variations import VariationManager, VariationCategoryChoice
from .models import Product , BaseModel



class Variation(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE  ,related_name="variations")
    variation_category = models.CharField(max_length=128 , choices=VariationCategoryChoice.choices)
    variation_value = models.CharField(max_length=128)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

    class Meta:
        verbose_name_plural = "variations"
        verbose_name = "variation"
