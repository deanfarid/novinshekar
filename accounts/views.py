from django.urls.base import reverse_lazy
from products.models import FishingProducts
from products.models import Categury
from django.shortcuts import redirect , render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Comment, users
from .serializers import  UserLoginSerializer, UserLogoutSerializer
#from django.contrib.auth.models import users
from django.contrib import auth
from django.contrib import messages
from .import models , serializers , forms
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
import threading
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from jalali_date import datetime2jalali, date2jalali
from cart.models import Cart


#########################################################
#ارسال ایمیل به کاربر
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
#########################################################
#ارسال ایمیل از دامنه مشخص شده به کاربر
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'فعال سازی حساب'
    email_body = render_to_string('confirm_template.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()
#########################################################
#ثبت نام کاربر
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']

        if password1 == password2:
            if users.objects.filter(username=username).exists():
                messages.info(request,'کاربری با این مشخصات قبلا ثبت شده است')
                return redirect('accounts:register')
            elif users.objects.filter(email=email).exists():
                messages.info(request,'کاربری با این ایمیل قبلا ثبت شده است')
                return redirect('accounts:register')
            else:

                user = users.objects.create_user(username=username,password=password1,email=email, phonenumber = phonenumber)
                user.save()
                send_activation_email(user, request)
                messages.add_message(request, messages.SUCCESS,
                                 'ایمیل برای شما ارسال شد لطفا حساب خود را تایید کنید')
                return redirect('accounts:login')
    else:
        form = forms.UserCreationForm()
        return render(request, 'create_user.html', {'form': form})

    form = forms.UserCreationForm()
    messages.info(request,'لطفا فیلد ها را پر کنید')
    return render(request, 'create_user.html', {'form': form})
#########################################################
# ورود کاربر به سایت
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                                 'لطفا ایمیل خود را چک کرده و حساب کاربری خود را تایید کنید')
            return render(request, 'login.html',  status=401)

        if user is not None:
            auth.login(request,user)
            profile = models.ProfileModel.objects.get_or_create(user=request.user)
            return redirect('/')
        else:
            messages.info(request,'کاربری با این مشخصات یافت نشد')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')

#########################################################
#فعال سازی حساب کاربر
def activate_user(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = users.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             'حساب کاربری شما با موفقیت فعال گردید لطفا وارد شوید.')
        return redirect(reverse('accounts:login'))

    return render(request, 'authentication/activate-failed.html', {"user": user})


class Favorites(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        favorite = FishingProducts.objects.filter(favorites=self.request.user)
        order = Cart.objects.get(user=self.request.user)
        category = Categury.objects.all()
        context = {
                'favorite': favorite,
                'order':order,
                'category':category,
        }
        return render(self.request, 'savedproduct.html', context)


@login_required
def remove_favorite(request, id , *args):
    product = get_object_or_404(FishingProducts, id=id )
    remove_fav = models.FishingProducts.objects.filter(favorites=request.user)
    if remove_fav.exists():
        order = remove_fav[0]
        if order.favorites.exists():
            order_item = models.FishingProducts.objects.filter(favorites=request.user)[0]
            order_item.favorites.remove(*order_item.favorites.filter(*args))
            return redirect("accounts:favorites")

@login_required
def ProfileEditView(request):
    if request.method == 'POST':
        profile_form = forms.ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        order = Cart.objects.get(user=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('accounts:profile')
        else:
            return redirect('/')
    else:
        profile_form = forms.ProfileEditForm(instance=request.user.profile)
        order = Cart.objects.get(user=request.user)
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        category = Categury.objects.all()
        context = {
            'profile_form': profile_form ,
            'order':order ,
            'jalali_join':jalali_join,
            'category':category,
        }

    return render(request, 'profile.html',context)
    # if request.method =="POST":
    #     profileView = forms.ProfileEditForm(request.POST)
    #     if profileView.is_valid:
    #         profileView.save()
    # else:
    #     profileView = forms.ProfileEditForm()
    
    # context = {
    #     'profileView':profileView
    # }
    # return render(request , 'profile.html' , context)




def logout_view(request):
    auth.logout(request)
    return redirect('/')

def asd(request , id , *args , **kwargs):
    product = get_object_or_404(FishingProducts ,id=id)
    comments = product.comments.filter(is_active=True)
    new_comment = None
    if request.method == 'POST':
        commentform = forms.CommentForm(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
    else:
        commentform = forms.CommentForm()                   
        
    context = {
            'commentform':commentform,
            'comments':comments,
            'new_comment ':new_comment,
        }
    return render(request, 'asd.html', context)





