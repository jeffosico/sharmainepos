from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products_view, name="products"),
]

htmx_urlpatterns = [
    path('add-product/', views.add_product_view, name="add-product")
]

urlpatterns += htmx_urlpatterns