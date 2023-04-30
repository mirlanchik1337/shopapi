from django.contrib import admin
from product.models import Product as P
from product.models import Review as R
from product.models import Category as C


admin.site.register(P)
admin.site.register(R)
admin.site.register(C)

# Register your models here.
