
from .models import  MenuItem,  ItemsCategory
from django.views.generic import ListView
from django.shortcuts import render
# Create your views here.


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_app/menu_list.html'

def menu_list_view(request):

    item_list = MenuItem.objects.all()
    context = {'item_list': item_list,
                'item_categories':reversed(ItemsCategory.objects.all())},
                return render(request, 'menu_app/menu_list.html', context)
                }