from django.contrib import admin

from eshop_products_category.models import ProductCategory
from .models import Product, ProductGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'price','description', 'active')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
