class MenuListView(ListView):
    model = MenuItem
    template_name = 'items/menu_list.html'

def menu_list_view(request):
    item_list = MenuItem.objects.all()

    context = {'item_list': item_list,
                'item_categories':reversed(ItemsCategory.objects.all()),
                'item_categories_side_nav':reversed(ItemsCategory.objects.all())}

    return render(request, 'items/menu_list.html', context)


def menu_item_detail(request, **kwargs):
    item = MenuItem.objects.filter(id=kwargs.get('pk')).first()

    context = {'item':item}

    return render(request, 'items/item_details.html', context)