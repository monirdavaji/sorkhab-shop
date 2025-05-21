from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render
from .models import Product, ProductGallery
# from django.core.paginator import Paginator
from eshop_products_category.models import ProductCategory
from eshop_order.forms import UserOrderForm



# def product_list(request):
#     object_list = Product.objects.all()
#     paginator = Paginator(object_list, 1)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)
#
#     context = {'object_list': page_obj.object_list, 'page_obj': page_obj, 'paginator': paginator}
#     return render(request,'product/products_list.html',context)

class ProductListView(ListView):
    template_name = 'product/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = Product.objects.get_active_products()
        # for obj in queryset:
        #     obj.formatted_price = "{:,}".format(obj.price)
        return queryset

class ProductListByCategory(ListView):
    template_name = 'product/products_list.html'
    paginate_by = 3

    def get_queryset(self,*args,**kwargs):
        category_name =self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('محصولی با این کتگوری یافت نشد')
        return Product.objects.products_by_category(category_name)
# برای ریترن بالا هست پایینی هم میشه استفاده کرد
# category.products.all()

def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']
    new_order_form = UserOrderForm(initial={'product_id': product_id})
    # name = kwargs['name']
    product = Product.objects.get_by_id(product_id)
    # formatted_price = "{:,}".format(product.price)
    if product is None or not product.active:
        raise Http404('Product not found')

    product.visit_count += 1
    product.save()
    # related_products = Product.objects.filter(categories__in=product).distinct()
    product_categories = product.categories.all()
    product_list_in_same_category = Product.objects.filter(categories__in=product_categories).exclude(id=product.id).distinct()


    related_products = [product_list_in_same_category[i:i+3] for i in range(0, len(product_list_in_same_category), 3)]

    galleries = ProductGallery.objects.filter(product_id = product_id)
    galleries = [galleries[i:i+3] for i in range(0, len(galleries), 3)]

    context = {
        'product': product,
        # 'formatted_price': formatted_price
        'galleries': galleries,
        'related_products': related_products,
        'new_order_form': new_order_form
    }

    return render(request, 'product/product_detail.html',context)


class SearchProductsView(ListView):
    template_name = 'product/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
            # print(queryset)
            # return queryset
        else:
            return Product.objects.get_active_products()


def products_categories_partial(request):

    categories = ProductCategory.objects.all()
    context = {
        'categories' : categories,

    }
    return render(request, 'product/products_categories_partial.html', context)

