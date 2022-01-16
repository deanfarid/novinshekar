from django.shortcuts import render
from . import models
# Create your views here.

def blog_view_detail(request , id):
    blog_view = models.BlogContent.objects.get(id = id)
    context = {
    blog_view:'blog_view',
    }
    return render(request , 'blog.html' , context)