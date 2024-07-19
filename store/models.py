from django.db import models
from common.models import BaseModel
from common.file_path_renamer import PathAndRename

product_path_and_rename = PathAndRename("products/main/")
product_images_path_and_rename = PathAndRename("products/images/")
# Create your models here.
class ProductCategory(BaseModel):
    name = models.CharField(max_length=255,db_index=True, unique=True)
    slug = models.SlugField(max_length=255, unique=True , blank=True , null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"
        verbose_name = "Product Category"

class Product(BaseModel):
    category = models.ForeignKey(ProductCategory , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_path_and_rename , blank=True , null=True)
    name = models.CharField(max_length=255 , db_index=True , unique=True)
    slug = models.SlugField(max_length=255 , unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=16 , decimal_places=2)
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)

    @property
    def is_in_stock(self):
        return self.stock > 0


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"

class ProductImage(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="images")
    image = models.ImageField(upload_to=product_images_path_and_rename)

    def __str__(self):
        return f"{self.product.name} image"

    class Meta:
        verbose_name_plural = "Product Images"
        verbose_name = "Product Image"