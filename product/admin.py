from django.contrib import admin
from .models import Product, Category, Sale, Type

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Sale)