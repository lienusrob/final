


from django.forms import ModelForm, widgets
from django.forms import Textarea
from . import models 
from django import forms 
from 



# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
       
class ReviewsFrom(forms.ModelForm):
    class Meta: 
        model =models.AnonymousReview
        fields = ['name', 'details']
        # name = forms.CharField(max_length= 100)
        # details = forms.CharField(widget=forms.Textarea)
        # date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']