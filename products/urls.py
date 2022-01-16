from django.urls.conf import include
from rest_framework.viewsets import ViewSet
import products
from django.urls import path , re_path
from products import views


urlpatterns = [
    # path('',views.productview),
    path('products/category/minicategory/<slug:minicategory>/',views.minisearch , name='category'),
    path('products/category/<slug:category>/',views.category_searach , name='category_search'),
    path('',views.search_product),
    path('products/search/',views.search , name='search'),
    path('products/offers/',views.special_offer , name='offers'),
    path('products/product_detail/<int:pk>/like',views.ADDLike.as_view() , name = "like"),
    path('products/product_detail/<int:pk>/dislike',views.ADDDisLike.as_view() , name= "dislike"),
    path('products/product_detail/<int:id>/', views.product_detail , name='product_detail'),
    path('products/new/', views.newestproducts , name='new_products'),


]