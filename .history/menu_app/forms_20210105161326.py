from django import forms 
from .models import CartItem, Cart, Extras

class AddToCartForm (forms.ModelForm): 
    #cart = forms.ModelChoiceField(queryset = Cart.objects.filter(current = True), to_field_name = "user")
    class Meta: 
        model = CartItem
        exclude = ["cart"]

        
class ExtrasForm(forms.M):
    extras = forms.CharField(widget=forms.Textarea)
    class Meta: 
        model = Extras
        fields = '__all__'