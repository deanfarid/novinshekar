from django.urls import path , include
from . import views

app_name = 'blog'
urlpatterns = [
    path('help/<int:id>', views.blog_view_detail , name='blog_view_detail' ),
]
