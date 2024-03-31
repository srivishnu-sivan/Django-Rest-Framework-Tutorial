from django.contrib import admin
from products.models import *

# Register your models here.

class Productadmin(admin.ModelAdmin):
    model=Product
    
admin.site.register(Product)