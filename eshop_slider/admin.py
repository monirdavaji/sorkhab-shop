from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','description')


admin.site.register(Slider,SliderAdmin)

