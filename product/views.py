from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from product.forms import ProductForm
from .models import Product

@login_required(login_url='/login/')
def products_view(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'product/products.html', context)


def add_product_view(request):
    form = ProductForm(request.POST, request.FILES)
    name = request.POST.get('name')
    description = request.POST.get('description')
    size = request.POST.get('size')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    category = request.POST.get('category')
    type = request.POST.get('type')

    if category == "1":
        category = "Popsicle"
    if category == "2":
        category = "Sundae"
    if category == "3":
        category = "Mochi"

    if type == "1":
        type = "Frozen Foods"
    else:
        type = "Aice Ice Cream"

    if form.is_valid():
        form.save()
        return HttpResponse("<tr><td><input type='checkbox' id='checkthis'></td><td>"+name+"</td><td>"+description+"</td><td>"+size+"g</td><td>"+quantity+"</td><td>₱"+price+".00</td><td>"+category+"</td><td>Aice Ice Cream</td><td><a href='' style='color:rgb(89, 89, 255);'><i class='fas fa-plus'></i></a>&nbsp;&nbsp;&nbsp;<a href='' style='color:red;'><i class='fas fa-minus'></i></a></td></tr>")
    else:
        return HttpResponse("Error!")
        