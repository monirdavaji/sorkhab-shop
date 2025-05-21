from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserOrderForm
from .models import Order,OrderDetail
from eshop_product.models import Product
from django.db.models import F
from django.http import  Http404,HttpResponse
from zeep import Client





@login_required(login_url='/login')
def user_order_form(request):
    new_order_form = UserOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.get_or_create_unpaid_order(request.user)

        product_id = new_order_form.cleaned_data['product_id']
        count = new_order_form.cleaned_data['count']

        product = Product.objects.get_by_id(product_id=product_id)
        if product is None:
            raise Http404

        product_exists = order.items.filter(product_id=product.id).exists()
        if product_exists:
            order.items.filter(product_id=product.id).update(count=F('count') + count)

        else:
            order.items.create(product_id=product.id, count=count)
        messages.success(request, 'محصول با موفقیت به سبد خرید اضافه شد')

        # todo : redirect to panel user
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')

    return redirect('home')


@login_required(login_url='/login')
def user_order_view(request):
    context = {
        'order': None,
        'oder_details' : None
    }
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is not None:
        context['order'] = order
        sum_price = 0
        for item in order.items.all():
            sum_price += item.product.price * item.count
        sum_formated_price = "{:,}".format(sum_price)
        context['order_details'] = order.items.all()
        context['sum_formated_price'] = sum_formated_price

    return render(request,'order/user_open_order.html', context)
@login_required(login_url='/login')
def delete_product_from_order(request,*args,detail_id):
    order_detail = OrderDetail.objects.filter(id=detail_id,order__owner_id=request.user.id).first()
    if order_detail is None:
        raise Http404

    order_id = order_detail.order_id
    order_detail.delete()
    messages.success(request,f'محصول {order_detail.product.title} از سبد خرید شما حذف شد')
    order = Order.objects.filter(id=order_id).first()
    if order.items.count() == 0:
        order.delete()

    return redirect('user_order_view')






