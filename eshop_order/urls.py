from django.urls import path
from .views import user_order_form, user_order_view, delete_product_from_order

urlpatterns = [
    path('user-order-form', user_order_form, name='user_order_form'),
    path('open-order', user_order_view, name='user_order_view'),
    path('delete/<int:detail_id>', delete_product_from_order, name='delete_product_from_order'),

]

