"""
URL configuration for toplearn_eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from toplearn_eshop import settings
from .views import home_page, header, footer, about_us

urlpatterns = [
        path("", home_page, name="home"),
        path("", include('eshop_account.urls')),
        path("", include('eshop_product.urls')),
        path("", include('eshop_contact.urls')),
        path("", include('eshop_order.urls')),
        path("header", header, name="header"),
        path("footer", footer, name="footer"),
        path("about-us", about_us, name="about_us"),
       path('admin/', admin.site.urls),
]

handler_404 = 'toplearn_eshop.views.error_404_view'


if not settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)