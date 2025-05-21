from django.db import models
import os




def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext



def upload_to(instance, filename):
    name, ext = get_filename_ext(filename)
    return f"sliders/{instance.pk}-{instance.title}{ext}"




class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    link = models.URLField(max_length=100,verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_to, null=True, blank=True,verbose_name='تصویر')


    class Meta:
        verbose_name='اسلایدر'
        verbose_name_plural='اسلایدر ها'


    def __str__(self):
        return self.title
