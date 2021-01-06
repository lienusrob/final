from django import forms 
from .models import CartItem, Cart, Extras
from django.forms import mo

class AddToCartForm (forms.ModelForm): 
    #cart = forms.ModelChoiceField(queryset = Cart.objects.filter(current = True), to_field_name = "user")
    class Meta: 
        model = CartItem
        exclude = ["cart"]

        
class ExtrasForm(ModelForm):
    class Meta:
        model = Extras
        fields = "__all__"

