from django.db import models
from django.contrib.auth import get_user_model
from eshop_product.models import Product

User = get_user_model()



class OrderManager(models.Manager):
    def get_or_create_unpaid_order(self, user):
        order = self.filter(owner=user, is_paid=False).first()
        if order:
            return order
        return self.create(owner=user, is_paid=False)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='خریدار', related_name='orders')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    objects = OrderManager()


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید', related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول', related_name='order_items')
    price = models.IntegerField(verbose_name='قیمت محصول' , null=True, blank=True)
    count = models.IntegerField(verbose_name='تعداد' , default=1)

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'

    def __str__(self):
        return self.product.title

    @property
    def get_detail_sum_price(self):
        price = self.product.price * self.count
        return "{:,}".format(price)

