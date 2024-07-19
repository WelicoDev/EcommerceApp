from django.shortcuts import render
from django.views import View
from .models import Product , ProductCategory
from django.views.generic import ListView , DetailView
from .variations import Variation , VariationCategoryChoice

# Create your views here.
class StoreView(ListView):
    model = Product
    template_name = "store.html"
    context_object_name = "products"
    queryset = Product.objects.filter(is_available=True)

class StoreDetailView(DetailView):
    model = Product
    template_name = "product-detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["size_variations"] = Variation.objects.filter(product=product,
                                                                            variation_category=VariationCategoryChoice.SIZE)
        context["color_variations"] = Variation.objects.filter(product=product,
                                                                            variation_category=VariationCategoryChoice.COLOR)

        return context