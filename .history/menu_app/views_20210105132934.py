
from .models import  Cart, CartItem, MenuItem,  ItemsCategory, Order, Orders, generate_order_id, Extras
from account_app.models  import Profile
from .forms import AddToCartForm, ExtrasForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 
from django.utils import timezone

class MenuListView(ListView):
    model = MenuItem
    template_name = 'items/menu_list.html'

def menu_list_view(request):
    item_list = MenuItem.objects.all()

    context = {'item_list': item_list,
                'item_categories':reversed(ItemsCategory.objects.all()),
                'item_categories_side_nav':reversed(ItemsCategory.objects.all())}

    return render(request, 'menu_app/menu_list.html', context)

def home(request):
    category_menu = ItemsCategory.objects.all()
    context = {'category_menu': category_menu}
    return render (request, 'homepage.html', context)

def menu_item_detail(request, **kwargs):
    item = MenuItem.objects.filter(id=kwargs.get('pk')).first()

    context = {'item':item}

    return render(request, 'menu_app/item_details.html', context)


def new_order_info(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order, created = Order.objects.get_or_create(customer=user_profile.user, is_ordered=False)
    if created:
        order.ref_code = generate_order_id()
        order.save()
    context = {'order':order}

    return render(request, 'items/order_info.html', context)


    
def menu_details(request, name):
    category = ItemsCategory.objects.get(name=name)
    menu_details = MenuItem.objects.filter(category=category)
    context = {'menu_details':menu_details, 'category':name, 'user':request.user}    

    if request.method=="POST":
        form = AddToCartForm(request.POST or None)
        if form.is_valid():
            cart_item = form.save(commit = False)
            cart_item.cart = Cart.objects.get_or_create(user = request.user, current=True)[0] 
            cart_item.save()
    
        else: 
            print(form.errors)
        #messages.success(request, "Item"  "added to cart successfully!, please go to cart and check for items.")
    return render(request, ('menu_app/menu_list.html'), context) 

def cart(request):
    cart = Cart.objects.get(user=request.user, current=True)
    cart_items = CartItem.objects.filter(cart=cart)
    extras = Extras.objects.all()
    context = {'cart_items':cart_items, 'extras': extras}
    return render(request, 'menu_app/cart.html', context)

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect('homepage')

    
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect('view_cart')

def orders (request):
    cart = Cart.objects.get(user=request.user, current = True)
    cart_items = CartItem.objects.filter(cart__pk = cart.pk)

    if request.method == "POST":
        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            extra_item = Extras.objects.get(pk=key)
            cart.extras.add(extra_item)
    # = is assining value == is comparing. befroe we where comparing but not doing somethign with the output. 
    cart.current = False 
    cart.date_ordered= timezone.now()
    cart.save()
    orders= Orders (cart = cart)
    orders.save()
    cart = Cart(user=request.user)
    cart.save()
    context = {'order':orders}
    return render (request, 'menu/place_order.html', context)


            
