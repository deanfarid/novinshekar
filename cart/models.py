from django.db import models
from django.conf import settings
from products.models import FishingProducts

# Create your models here.
############################################################################
# سبد خریداری شده
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name = "کاربر")
    is_paid = models.BooleanField(default=False,verbose_name = "خریداری شده " , blank=True)
    items = models.ManyToManyField('CartItem' , verbose_name="کالاها",related_name='items')
    start_date = models.DateTimeField(auto_now_add=True , verbose_name="زمان شروع سفارش")
    ordered_date = models.DateTimeField(verbose_name="زمان تحویل" , null=True)
    ordered = models.BooleanField(default=False, verbose_name="ثبت شده")

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def __str__(self):
        return self.user
############################################################################
#محصولات درون سبد خرید
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name = "کاربر", default=1)
    product = models.ForeignKey(FishingProducts, on_delete=models.CASCADE,verbose_name = "محصول")
    quantity = models.IntegerField(verbose_name = "تعداد" , default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_discount_item_price(self):
        return self.quantity * self.product.price_discounted

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.product.price_discounted:
            return self.get_discount_item_price()
        return self.get_total_item_price()