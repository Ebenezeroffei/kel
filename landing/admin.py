from django.contrib import admin
from .models import Product,UserCartItems

# Register your models here.
admin.site.register(Product)
admin.site.register(UserCartItems)