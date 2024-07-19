from django.contrib import admin
from store.models import ProductCategory , Product , ProductImage
from django.utils.html import format_html
from store.variations import Variation
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 8

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "name", "price", "category",'stock', 'is_available', 'is_active', 'created_at')
    list_filter = ("category", "is_available", 'is_active', 'created_at')
    search_fields = ("name", "category__name")
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ("price", "is_available", 'stock', 'is_active')
    autocomplete_fields = ("category",)
    inlines = [ProductImageInline]

    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.image.url}'>")

    thumbnail.short_description = "Thumbnail"

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ("product", "variation_category","variation_value", "is_active")
    list_editable = ("is_active",)
    list_filter = ("product", "variation_category", "is_active")
    search_fields = ("product__name", "variation_value")
    autocomplete_fields = ("product",)