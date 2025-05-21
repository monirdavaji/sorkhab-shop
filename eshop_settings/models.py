from django.db import models
import os



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext



def upload_to_logo(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"logo/{name}{ext}"




class SiteSetting(models.Model):
    site_name_persian = models.CharField(max_length=255,verbose_name='نام سایت به فارسی ')
    site_name_english = models.CharField(max_length=200,verbose_name='نام سایت به انگلیسی')
    logo = models.ImageField(upload_to=upload_to_logo,verbose_name='لوگو',blank=True,null=True)
    address = models.CharField(max_length=500,verbose_name='آدرس')
    phone = models.CharField(max_length=20,verbose_name='تلفن')
    mobile = models.CharField(max_length=20,verbose_name='موبایل')
    fax = models.CharField(max_length=20,verbose_name='فکس')
    email = models.EmailField(max_length=50,verbose_name='ایمیل')
    location_lat = models.DecimalField(max_digits=9, decimal_places=7)
    location_lng = models.DecimalField(max_digits=9, decimal_places=7)
    copy_right = models.CharField(max_length=300,verbose_name='کپی رایت')
    about_us = models.CharField(max_length=500,verbose_name= 'درباره ما' ,blank=True,null=True)


    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'همه ی قسمت های تنظیمات'


    def __str__(self):
        return self.site_name_persian
