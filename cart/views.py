from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from products.models import FishingProducts
from . import models
from django.contrib.auth.decorators import login_required
from accounts.models import ProfileModel
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from products. models import Categury



# Create your views here.



class OrderSummaryView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):

        try:
            order = models.Cart.objects.get(user=self.request.user, ordered=False)
            oror = models.Cart.objects.get(user=self.request.user)
            category = Categury.objects.all()
            context = {
                'object': order,
                'oror':oror,
                'category':category
            }
            return render(self.request, 'peigiri.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("cart:usercart")

############################################################################################
@login_required
def add_to_cart(request, id):
    product = get_object_or_404(FishingProducts, id=id )
    order_item , created = models.CartItem.objects.get_or_create(
        product = product,
        user = request.user,
        ordered = False
    )
    order_qs = models.Cart.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(product__id=product.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("cart:usercart")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("cart:usercart")
    else:
        ordered_date = timezone.now()
        order = models.Cart.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("cart:usercart")
############################################################################################
@login_required
def remove_from_cart(request, id):
    product = get_object_or_404(FishingProducts, id=id )
    order_qs = models.Cart.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__id=product.id).exists():
            order_item = models.CartItem.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \""+order_item.product.name+"\" remove from your cart")
            return redirect("cart:usercart")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("product_detail", id=id)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("product_detail", id = id)
############################################################################################
@login_required
def reduce_quantity_item(request, id):
    product = get_object_or_404(FishingProducts, id=id )
    order_qs = models.Cart.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__id=product.id).exists() :
            order_item = models.CartItem.objects.filter(
                product = product,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("cart:usercart")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("cart:usercart")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("cart:usercart")


        


