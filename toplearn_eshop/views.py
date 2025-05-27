from django.conf import settings
from django.shortcuts import render
from eshop_slider.models import Slider
from eshop_settings.models import SiteSetting
from eshop_product.models import Product

def home_page(request):
    sliders = Slider.objects.all()
    most_visit = Product.objects.all().order_by('-visit_count')[:8]
    most_visit = [most_visit[i:i+4] for i in range(0, len(most_visit), 4)]

    latest_visit = Product.objects.all().order_by('-id')[:8]
    latest_visit = [latest_visit[i:i+4] for i in range(0, len(latest_visit), 4)]


    context = {
        'data' : 'new_data',
        'sliders' : sliders,
        'most_visit' : most_visit,
        'latest_visit' : latest_visit

    }
    return render(request,'home_page.html',context)


def header(request,*args,**kwargs):
    setting = SiteSetting.objects.first()
    context = {
        'setting' : setting
    }
    return render(request,'shared/Header.html',context)

def footer(request,*args,**kwargs):
    setting = SiteSetting.objects.first()
    context = {
        'setting' : setting
    }
    return render(request,'shared/Footer.html',context)

def about_us(request):
    setting = SiteSetting.objects.first()
    context = {
        'setting': setting
    }
    return render(request, 'about_us.html', context)

def error_404_view(request,exception):
    return render(request, '404.html', status=404)