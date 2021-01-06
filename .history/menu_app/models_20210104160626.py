
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import random
import string
from datetime import date, datetime



class ToppingsCategory(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 4, decimal_places=2, default=0)
    category = models.ForeignKey(ToppingsCategory, on_delete = models.PROTECT, default=None)
   
    def __str__(self):
        return self.name


class ItemsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=22)
    price = models.DecimalField(max_digits = 4, decimal_places=2)
    category = models.ForeignKey(ItemsCategory, on_delete = models.PROTECT)
    detail = models.TextField(max_length=1000, default = ' ')
    # toppings = models.ManyToManyField(Topping, blank=True)
    #image = models.ImageField(default=None, upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name

class Cart (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current = models.BooleanField(default=True)
    date_ordered = models.DateTimeField(default= datetime.now, null = True, blank= True)

    def __str__ (self): 
        return user.username 

class CartItem (models.Model):
    add_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)

    def __str__(self):
        return self.add_item.name

#remove dont need 
class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits = 4, decimal_places=2, default=0)
    order_item_order = models.ForeignKey('menu_app.Order', on_delete=models.CASCADE, null=True)
   #toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return self.item.name

    def get_item_price(self):
        self.price = sum(topping.price for topping in self.toppings.all()) + self.item.price


    def get_all_topping_categories(self):
        categories = []
        for topping in self.toppings.all():
            if not topping.category in categories:
                categories.append(topping.category)
        return categories

class 


#old need to remove 
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now)
    items = models.ManyToManyField(MenuItem)
    order_items = models.ManyToManyField(OrderItem)
    total = models.DecimalField(max_digits = 6, decimal_places=2, null=True)
    is_ordered = models.BooleanField(default=False)
    pickup_time = models.DateTimeField(default=timezone.now)
    special_instructions = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f'Order #{self.id} - {self.customer.username}'

    # # url to redirect to when submitting order form
    # def get_absolute_url(self):
    #     return reverse('orders:order_detail', kwargs={'pk':self.pk})

    # returns the sum of each item price in order and assigns it to self.total
    def get_order_total(self):
        self.total = sum(order_item.price for order_item in self.order_items.all())

    def get_cart_items(self):
        return self.items.all()


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str
    # class Meta():
    #     ordering = ['-date_ordered']


