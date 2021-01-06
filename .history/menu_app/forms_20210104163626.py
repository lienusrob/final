from django import forms 
from .models import CartItem, Cart

class AddToCartForm (forms.ModelForm): 
    cart = forms.ModelChoiceField(queryset = Cart.objects.filter(current = True), to_field_name = "user")
    class Meta: 
        model = CartItem
        fields = "__all__"

