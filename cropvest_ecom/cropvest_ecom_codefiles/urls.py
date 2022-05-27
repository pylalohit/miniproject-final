from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('viewsellers',views.viewsellers, name='viewsellers'),
    path('signupverifying',views.signupverifying,name='signupverifying'),
    path('loginverifying',views.loginverifying,name='loginverifying'),
    path('mystore',views.mystore,name='mystore'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addproductvalidate',views.addproductvalidate,name='addproductvalidate'),
    path('updateproduct',views.updateproduct,name='updateproduct'),
    path('selectseller',views.selectseller,name='selectseller'),
    

    path('authenticate',views.authenticate,name='authenticate'),
    path('logout',views.logout,name='logout')
]