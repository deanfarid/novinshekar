from re import S, T
import products
from django.db.models.deletion import PROTECT
from extensions.utils import jalali_converter
from django.db import models
from django.db.models import Sum
from products.models import FishingProducts
from django.utils.timezone import now
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings


############################################################################
##شخصی سازی مدل پیش ساخته کاربر جنگو(User)
class users(AbstractUser):
    phonenumber = models.CharField(_('شماره تماس'),unique=True,max_length=11,null=True)
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return "{} -{}".format(self.username, self.email)
############################################################################
#مدل کامنت و ریپلای
class Comment(models.Model):
    product = models.ForeignKey(FishingProducts, on_delete=models.CASCADE, related_name='comments',verbose_name = "محصول" , null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name = "کاربر", null=True )
    content = models.TextField(max_length=255,verbose_name = "محتوا")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "تاریخ")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,verbose_name = "نظر")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
############################################################################
class ProfileModel(models.Model):
    name = models.CharField(max_length=100 , null=True , verbose_name='نام و نام خانوادگی')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='کاربر' , null=True , related_name='profile')
    location = models.CharField(_('موقعیت مکانی'),max_length=300 , null=True)
    home = models.BigIntegerField(_('تلفن ثابت '),unique=True , null=True)
    zipcode = models.BigIntegerField(_('کد پستی ‍') , null=True)
    melicode = models.BigIntegerField(_('کد ملی'),unique=True , null=True)
    email = models.EmailField(_('ایمیل'),max_length=250 , null=True)
    favorites = models.ManyToManyField(FishingProducts , verbose_name='نشان شده ها' , related_name='favorited_by')
    birthday = models.DateTimeField(auto_now_add=False , null=True)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"

    def jcreated(self):
        return jalali_converter(self.created)
############################################################################
#مدل لیست کالا ها و وضعیت محصول
class MyWishList(models.Model):
    listproduct = models.ManyToManyField(FishingProducts , verbose_name='لیست کالا ها')
    certain_user = models.ForeignKey('users',on_delete=models.CASCADE,verbose_name = "کاربر مورد نظر")
    choices_From = (
        ('01',' در حال پردازش'),
        ('02',' تحویل شده '),
        ('03','مرجوعی'),
        ('04',' لغو شده '),
    )

    class Meta:
        verbose_name = " لیست کالا ها"
        verbose_name_plural = "لیست های کالا ها "
    status = models.CharField(_('وضعیت محصول'), choices=choices_From , max_length=20 , null=True)


 
 
