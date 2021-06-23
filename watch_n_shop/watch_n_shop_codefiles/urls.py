from django.urls import path
from . import views


urlpatterns = [
path('',views.cover,name='cover'),
path('buyerlogin',views.buyerlogin,name='buyerlogin'),
path('sellerlogin',views.sellerlogin,name='sellerlogin'),
path('buyerloginvalidate',views.buyerloginvalidate,name='buyerloginvalidate'),
path('buyersignupvalidate',views.buyersignupvalidate,name='buyersignupvalidate'),
path('sellerloginvalidate',views.sellerloginvalidate,name='sellerloginvalidate'),
path('sellersignupvalidate',views.sellersignupvalidate,name='sellersignupvalidate'),
path('buyerlogout',views.buyerlogout,name='buyerlogout'),
path('viewusers',views.viewusers,name='viewusers'),
path('addproduct',views.addproduct,name='addproduct'),
path('addproductvalidate',views.addproductvalidate,name='addproductvalidate'),
path('sellerlogout',views.sellerlogout,name='sellerlogout'),
path('sellerprofile',views.sellerprofile,name='sellerprofile'),
path('selectseller',views.selectseller,name='selectseller'),
path('buyerloginvalidate1',views.buyerloginvalidate1,name='buyerloginvalidate'),
path('sellerloginvalidate1',views.sellerloginvalidate1,name='sellerloginvalidate1'),
path('wish_list',views.wish_list,name='wishlist'),
]