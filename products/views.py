from django.db.models.lookups import IContains
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from accounts.serializers import CommentSerializer
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse 
# from rest_framework import viewsets
from rest_framework import generics , viewsets
from rest_framework.serializers import Serializer
from . import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http.request import HttpRequest 
from rest_framework.renderers import JSONRenderer
from accounts.models import Comment, users
from django.http import request
from . import forms
from django.views.decorators.csrf import csrf_protect
from .filters import ProductFilter
from .models import Categury, FishingProducts, MiniCategury
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator
from cart.models import Cart
from math import ceil, floor
from accounts.forms import CommentForm
from blog.models import BlogContent


# Create your views here.


############################################################################
#تابع لایک کردن محصولات توسط کاربر
class ADDLike(LoginRequiredMixin, View):
    def post(self , request , pk ,*args , **kwargs):
        product = FishingProducts.objects.get(pk=pk)

        is_dislike = False

        for dislike in product.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            product.dislikes.remove(request.user)

        is_like = False

        for like in product.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            product.likes.add(request.user)

        if is_like:
            product.likes.remove(request.user)
        next = request.POST.get('next' , '/')
        return HttpResponseRedirect(next)
############################################################################
# تابع دیسلایک کردن محصولات توسط کاربر
class ADDDisLike(LoginRequiredMixin, View):
    def post(self , request , pk ,*args , **kwargs):
        product = FishingProducts.objects.get(pk=pk)

        is_like = False

        for like in product.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            product.likes.remove(request.user)

        is_dislike = False

        for dislike in product.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if not is_dislike:
            product.dislikes.add(request.user)

        if is_dislike:
            product.dislikes.remove(request.user)
        
        next = request.POST.get('next' , '/')
        return HttpResponseRedirect(next)

############################################################################
def category_searach(request , category ):
    pro = models.FishingProducts.objects.filter(category__slug = category)
    products = models.FishingProducts.objects.all()
    minicategory = MiniCategury.objects.all()
    category = Categury.objects.all()
    paginator = Paginator(pro, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    pro_compelete_list = paginator.get_page(page_number)
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'pro_compelete_list':pro_compelete_list,
        'order':order,
        
    }
        return render(request,'category_search.html',context)

    context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'pro_compelete_list':pro_compelete_list,
    }
    return render(request,'category_search.html',context)


############################################################################
#لیست محصولات
def product_category(request,category ):
    products = models.FishingProducts.objects.all()
    pro = models.FishingProducts.objects.filter(category__slug = category)
    tags = models.Tags.objects.all()
    comments = Comment.objects.all()
    category = Categury.objects.all()
    minicategory = MiniCategury.objects.all()
    f = ProductFilter(request.GET, queryset=models.FishingProducts.objects.all())
    newestproduct = models.FishingProducts.objects.all()
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
                'tags': tags ,
                'products':products,
                'filter': f,
                'comments':comments,
                'category':category,
                'minicategory':minicategory,
                'newestproduct':newestproduct,
                'pro':pro,
                'order':order,
                }
        return render(request, 'mahsool1.html', context)

    context = {
                'tags': tags ,
                'products':products,
                'filter': f,
                'comments':comments,
                'category':category,
                'minicategory':minicategory,
                'newestproduct':newestproduct,
                'pro':pro,

                }
    return render(request, 'mahsool1.html', context)

############################################################################
#تابع سرچ کردن محصولات
def search_product(request):
    """ search function  """
    products = FishingProducts.objects.all()
    newestproduct = models.FishingProducts.objects.all().order_by('-created')
    category01 = models.MiniCategury.objects.filter(parent__title__in = ['چوب ماهیگیری'])
    category02 = models.MiniCategury.objects.filter(parent__title__in = ['طعمه ها'])
    category03 = models.MiniCategury.objects.filter(parent__title__in = ['چرخ ماهیگیری'])
    category04 = models.MiniCategury.objects.filter(parent__title__in = ['انواع قلاب'])
    category05 = models.MiniCategury.objects.filter(parent__title__in = ['لوازم جانبی ماهیگیری'])
    img = models.mainpageimages.objects.all()
    blog_view = BlogContent.objects.all()

    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context ={
        'products':products,
        'newestproduct':newestproduct,
        'category01':category01,
        'category02':category02,
        'category03':category03,
        'category04':category04,
        'category05':category05,
        'order':order,
        'img':img,
        'blog_view':blog_view,
        }
        return render(request, 'mainpage.html',context) 

    context ={
        'products':products,
        'newestproduct':newestproduct,
        'category01':category01,
        'category02':category02,
        'category03':category03,
        'category04':category04,
        'category05':category05,
        'img':img,
        'blog_view':blog_view,



        }
    return render(request, 'mainpage.html',context) 

############################################################################

def minisearch(request , minicategory ):
    category01 = models.MiniCategury.objects.filter(parent__title__in = ['چوب ماهیگیری'])
    category02 = models.MiniCategury.objects.filter(parent__title__in = ['طعمه ها'])
    category03 = models.MiniCategury.objects.filter(parent__title__in = ['چرخ ماهیگیری'])
    category04 = models.MiniCategury.objects.filter(parent__title__in = ['انواع قلاب'])
    category05 = models.MiniCategury.objects.filter(parent__title__in = ['لوازم جانبی ماهیگیری'])
    products = FishingProducts.objects.all()
    pro = FishingProducts.objects.filter(minicategory__slug = minicategory)
    paginator = Paginator(pro, 12) # Show 12 contacts per page.
    page_number = request.GET.get('page')
    pro_compelete_list = paginator.get_page(page_number)
    category = Categury.objects.all()
    minicategory = MiniCategury.objects.all()
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
            'pro_compelete_list':pro_compelete_list,
            'products':products,
            'category':category,
            'minicategory':minicategory,
            'pro':pro,
            'category01':category01,
            'category02':category02,
            'category03':category03,
            'category04':category04,
            'category05':category05,
            'order':order,        
        }
        return render(request, 'minicategory_search.html',context) 

    context = {
        'pro_compelete_list':pro_compelete_list,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'pro':pro,
        'category01':category01,
        'category02':category02,
        'category03':category03,
        'category04':category04,
        'category05':category05,

    }
    return render(request, 'minicategory_search.html',context) 


############################################################################
def search(request):
    if request.method =='GET':
        q = request.GET.get("search")
        product_list = models.FishingProducts.objects.filter(Q(name__contains = q) | Q(category__title__contains=q) | Q(minicategory__title__contains=q))
        paginator = Paginator(product_list, 12) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        product_compelete_list = paginator.get_page(page_number)
    product_list = models.FishingProducts.objects.filter(Q(name__contains = q) | Q(category__title__contains=q) | Q(minicategory__title__contains=q))
    products = FishingProducts.objects.all()
    paginator = Paginator(product_list, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    product_compelete_list = paginator.get_page(page_number)
    minicategory = MiniCategury.objects.all()
    category = Categury.objects.all()
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
            'product_compelete_list':product_compelete_list,
            'products':products,
            'category':category,
            'minicategory':minicategory,
            'q': q,
            'order':order,
        }
        return render (request,'mahsool1.html',context)

    context = {
            'product_compelete_list':product_compelete_list,
            'products':products,
            'category':category,
            'minicategory':minicategory,
            'q': q,

        }
    return render (request,'mahsool1.html',context)
############################################################################
def special_offer(request):
    pro = FishingProducts.objects.filter(special_offer = True)
    products = FishingProducts.objects.all()
    category = Categury.objects.all()
    minicategory = MiniCategury.objects.all()
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'order':order,
    }
        return render (request,'special_offer.html',context)
    context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
    }
    return render (request,'special_offer.html',context)
############################################################################
def catcat(request , slug):
    catcat = Categury.objects.get(slug=slug)
    products = FishingProducts.objects.all()
    category = Categury.objects.all()
    minicategory = MiniCategury.objects.all()
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
        'catcat':catcat,
        'category':category,
        'products':products,
        'minicategory':minicategory,
        'order':order,
    }
        return render (request,'mahsool1.html',context)

    context = {
        'catcat':catcat,
        'category':category,
        'products':products,
        'minicategory':minicategory,
    }
    return render (request,'mahsool1.html',context)
############################################################################
def product_detail(request , id):
    product_detail = models.FishingProducts.objects.get(id = id)
    all_products = models.FishingProducts.objects.all
    kayval = models.KeyVal.objects.all()
    images = product_detail.image.all()
    comments = Comment.objects.all()
    category = Categury.objects.all()
    likes = product_detail.likes.all().count()
    dislikes = product_detail.dislikes.all().count()
    sum = (likes/(likes+dislikes))*100
    final = ceil(sum)
    comments = product_detail.comments.filter(is_active=True)
    new_comment = None
    a = 'ضعیف'
    b = 'خوب'
    c = 'عالی'

    if request.method == 'POST':
        product_detail.favorites.add(request.user)
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.product = product_detail
            new_comment.author = request.user
            new_comment.save()
        context = {
            'product_detail':product_detail,
        }
    else:
        commentform = CommentForm()   

    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
            'product_detail':product_detail,
            'kayval':kayval,
            'images':images,
            'comments':comments,
            'all_products':all_products,
            'order':order,
            'final':final,
            'category':category,
            'a':a,
            'b':b,
            'c':c,
            'commentform':commentform,
            'comments':comments,
            'new_comment ':new_comment,

        }
        return render(request, 'mahsool2.html', context)

    context = {
            'product_detail':product_detail,
            'kayval':kayval,
            'images':images,
            'comments':comments,
            'all_products':all_products,
            'final':final,
            'category':category,
            'commentform':commentform,
            'comments':comments,
            'new_comment ':new_comment,
        }

    return render(request, 'mahsool2.html', context)

def newestproducts(request):
    pro = FishingProducts.objects.all().order_by('-updated')
    products = FishingProducts.objects.all()
    category = Categury.objects.all()
    minicategory = MiniCategury.objects.all()
    paginator = Paginator(pro, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    product_compelete_list = paginator.get_page(page_number)
    if request.user.is_authenticated:
        order = Cart.objects.get(user=request.user)
        context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'order':order,
        'product_compelete_list':product_compelete_list,
    }
        return render (request,'newest_products.html',context)
    context = {
        'pro':pro,
        'products':products,
        'category':category,
        'minicategory':minicategory,
        'product_compelete_list':product_compelete_list,
    }
    return render (request,'newest_products.html',context)