
# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Profile, Contact
from .forms import RegistrationForm
#from .forms import ContactForm
from . import forms 
from django.views.generic import ListView, DetailView

# Create your views here.
def user_register(request):
    
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account Created Succesfully For  " + username)
            return redirect('user_login')    
        else:
           return render(request, 'registration/signup.html', {'form': form })

    return render(request, 'registration/signup.html', {'form': form })


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, "User logged in as " + username)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Login not possible")
    return render(request, 'login.html', {'form':form})

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    context = {'from_class':form_class}
    success_url = reverse_lazy('login')   

    def form_valid (self, form_class):
        form_class.save()
        return super().form_valid(form_class)

class HomeView (TemplateView):
    template_name = "homepage.html"

class UserListView(ListView):
     model = Profile 

class DetailView (DetailView): 
    model= Profile 

# contact from

# class ContactCreate(CreateView):
#     model = Contact
#     form_class = ContactForm
#     success_url = reverse_lazy("thank_you")

# def thank_you(request): 
#     return render (request, ("thank_you.html"))

def create_review(request):
    form = forms.ReviewsFrom()
    return render (request, 'homepage.html', {'form':form})
