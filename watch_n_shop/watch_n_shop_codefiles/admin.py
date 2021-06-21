from watch_n_shop_codefiles.models import userdetails
from django.contrib import admin
from .models import product
from .models import userdetails
from .models import wishlist
# Register your models here.
admin.site.register(product)
admin.site.register(userdetails)
admin.site.register(wishlist)