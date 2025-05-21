from django.contrib import admin

from eshop_products_category.models import ProductCategory



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name')


admin.site.register(ProductCategory, ProductCategoryAdmin)