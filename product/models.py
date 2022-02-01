from email.policy import default
from pydoc import describe
from django.db import models


class Category(models.Model):
    CATEGORIES = [
        ('popsicle','Popsicle'),
        ('sundae','Sundae'),
        ('mochi','Mochi'),
    ]
    name = models.CharField(choices=CATEGORIES, blank=False, null=False, max_length=100)
    
    def __str__(self):
        return self.name

    def category_verbose(self):
        return dict(Category.CATEGORIES)[self.name]

class Type(models.Model):
    TYPES = [
        ('frozen-foods','Frozen Foods'),
        ('aice-ice-cream','Aice Ice Cream')
    ]
    name = models.CharField(choices=TYPES, blank=False, null=False, max_length=100)

    def __str__(self):
        return self.name

    def type_verbose(self):
        return dict(Type.TYPES)[self.name]

class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    description = models.TextField(blank=True, null=True, max_length=500)
    size = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)
    quantity = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=1)
    price = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg")

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category.category_verbose()
    
    def get_type(self):
        return self.type.type_verbose()


    

    
class Sale(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    quantity = models.CharField(blank=False, null=False, max_length=100)
    total = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    



