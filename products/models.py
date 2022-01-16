from django.db import models
from django.db.models.deletion import PROTECT
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from extensions.utils import jalali_converter
from django.urls import reverse
import django_filters
from django_filters import rest_framework as filters

# Create your models here.
############################################################################
#محصولات اینگونه درون دیتا بیس قرار میگیرند
class FishingProducts(models.Model):
    name = models.TextField(_("نام محصول"),max_length=100)
    descriptions =models.TextField(_("توضیحات"), max_length=100000)
    price = models.IntegerField(_("قیمت"))
    price_discounted = models.IntegerField(_("قیمت با تخفیف") , null=True , blank=True)
    image = models.ManyToManyField('Images', verbose_name='عکس ها' , related_name='image')
    picture = models.ImageField(verbose_name='عکس های صفحع اصلی',upload_to = 'pics/')
    numbers = models.IntegerField(_("تعداد"), blank=True , null=True)
    rate = models.ForeignKey('feedback', on_delete=models.SET_DEFAULT, null=True, default = "NA", blank=True, verbose_name='امتیاز')
    slug = models.SlugField(unique=True , blank=True, verbose_name='اسلاگ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True, verbose_name='اپدیت شده')
    category = models.ForeignKey('Categury',on_delete=models.PROTECT,null=True, verbose_name='دسته بندی')
    minicategory = models.ForeignKey('MiniCategury',on_delete=models.PROTECT, null=True)
    tags = TaggableManager(help_text='برای جدا کردن تگ ها از "," استفاده کنید')
    tag = models.ManyToManyField('Tags', verbose_name='تگ ها')
    likes = models.ManyToManyField(to='accounts.users', verbose_name='لایک')
    dislikes = models.ManyToManyField(to='accounts.users', verbose_name='دیس لایک', related_name='dislike')
    special_offer = models.BooleanField(verbose_name='پیشنهاد شگفت انگیز' , null=True)
    kayvalue = models.ForeignKey('Dicty', on_delete=models.CASCADE , verbose_name='ویژگی',null=True)
    specials = models.ManyToManyField('KeyVal' , related_name= 'specials',verbose_name='ویژگی های خاص')
    favorites = models.ManyToManyField(to='accounts.users' , verbose_name='علاقه مندی ها' , related_name='faves')
    stock = models.BooleanField(verbose_name='موجود' , default=1)
    # dislike = models.ManyToManyField(User, verbose_name='دیسلایک')

    def __str__(self):
        return self.name

    #پر شدن خودکار اسلاگ slug
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def jcreated(self):
        return jalali_converter(self.created)

    def jupdated(self):
        return jalali_converter(self.updated)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})

    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={"id" : self.id})

    def get_remove_from_cart_url(self):
        return reverse("cart:remove-from-cart", kwargs={
            "id" : self.id
        })

    
    
    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'
############################################################################
#در این قسمت برای ایجاد دیکشنری از 2 مدل زیر کمک میگیریم
class Dicty(models.Model):
    Details = models.CharField(_("مشخصه"),max_length=50)
    def __str__(self):
        return self.Details
    
    class Meta:
        verbose_name='نوع محصول'
        verbose_name_plural=' نوع محصولات'
############################################################################
#ادامه ی دیکشنری
class KeyVal(models.Model):
    container = models.ForeignKey('Dicty', db_index=True,on_delete=PROTECT,)
    key = models.CharField(_("مشخصه"),max_length=240, db_index=True)
    value = models.CharField(_("مقدار"),max_length=240, db_index=True)
    important = models.BooleanField(verbose_name='ویژگی مهم' , null=True , default=2)
    def __str__(self):
        # return '('+ str(self.key)+':'+ str(self.value)+' , مهم بودن :'+ str(self.important)+')'
        return self.key + ":" + self.value 

    class Meta:
        verbose_name='مشخصه ی فنی'
        verbose_name_plural='مشخصات فنی'

############################################################################
class Images(models.Model):
    img = models.ImageField(_("عکس"), upload_to = 'pics/')
    def __str__(self):
        return self.img.name
    class Meta:
        verbose_name='عکس'
        verbose_name_plural='عکس ها'

############################################################################
# امتیاز دهی
class feedback(models.Model):
    SCORE_CHOICES = zip(range(6), range(6) )    
    user = models.CharField(_("کاربر"),max_length=50, null= True, default='anonymous user')
    item = models.ForeignKey('FishingProducts', on_delete=models.CASCADE, null= True)
    rating = models.PositiveSmallIntegerField(_("امتیاز"),choices=SCORE_CHOICES, blank=False)

    def __str__(self):
        return 'Rating(Item ='+ str(self.item)+', Stars ='+ str(self.rating)+')'
    
    class Meta:
        verbose_name='باز خورد'
        verbose_name_plural='باز خورد ها'
############################################################################
class Categury(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(verbose_name='عنوان لاتین',null=True)
    
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
    def __str__(self):
        return self.title
############################################################################
class MiniCategury(models.Model):
    parent = models.ForeignKey('Categury',on_delete=models.CASCADE)
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(verbose_name='عنوان لاتین',null=True , unique=True)
    
    class Meta:
        verbose_name=' ریز دسته بندی'
        verbose_name_plural='ریز دسته بندی ها'
    def __str__(self):
        return self.title
############################################################################
class Tags(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(unique=True , blank=True)

    class Meta:
        verbose_name='تگ'
        verbose_name_plural='تگ ها'

        #پر شدن خودکار اسلاگ slug
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
############################################################################
class PriceField(models.Model):
    choices_From = (
        ('0',' افزایشی'),
        ('1','کاهشی'),
    )

    status = models.CharField(_('وضعیت '), choices=choices_From , max_length=20 , null=True)

class mainpageimages(models.Model):
    image = models.ImageField(verbose_name='عکس ها', upload_to = 'pics/')