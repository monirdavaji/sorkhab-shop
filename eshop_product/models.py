
from eshop_products_category.models import ProductCategory
from django.db import models
import os
from django.db.models import Q



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_to(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"products/{instance.pk}-{instance.title}{ext}"

def upload_gallery_to(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"products/gallery/{instance.pk}-{instance.title}{ext}"




class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def products_by_category(self,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name,active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query)|
                Q(tags__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()





class Product(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_to, null=True, blank=True,verbose_name='تصویر')
    active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField(ProductCategory,blank=True,verbose_name='دسته بندی ها', related_name='products')
    visit_count = models.IntegerField(default=0,verbose_name='تعداد بازدید')

    objects = ProductManager()

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ','-')}"

    @property
    def formatted_price(self):
        return "{:,}".format(self.price)

class ProductGallery(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_to, verbose_name='تصویر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')


    class Meta:
        verbose_name='تصویر'
        verbose_name_plural=' تصاویر'


    def __str__(self):
        return self.title

