from .models import Extras, ItemsCategory, MenuItem, Order, OrderItem, Topping, ToppingsCategory, Cart, CartItem,
Extras
from django.contrib import admin

# Register your models here.
admin.site.register(ToppingsCategory)
admin.site.register(Topping)
admin.site.register(ItemsCategory)
admin.site.register(MenuItem)
admin.site.register(OrderItem)
#admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Extras)
