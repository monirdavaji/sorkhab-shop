from django.contrib import admin
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title' , 'slug' , 'timestamp','active']
    # این پایینی باعث میشه وقتی slug داره از رو title ساخته میشه به صورت زنده ساخته بشه و دیده بشه
    prepopulated_fields = {'slug': ('title',)}
#


admin.site.register(Tag, TagAdmin)





