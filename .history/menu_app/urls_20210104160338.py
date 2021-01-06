
# from project.account_app.views import HomeView
from django.urls import path
from . import views
from .views import view_cart, add_to_cart, adjust_cart
urlpatterns = [

#path('', views.menu_list_view(template_name = 'menu_app/menu_list.html'), name = 'menu_list'),
#path('menu/', views.menu_list_view, name = 'menu_list'),
#path ('', views.menu_category, name = 'menu_category'), 
# path ('admin_page/', views.MenuItem, name = 'menu_item'),
# path ('', views.home, name = "home"),
# path ('cart/', views.cart, name = "cart"),
# path ('<str:name>/', views.menu_details, name = 'menu_details'),
path('', views.home, name="home"),  
path('cart/', views.cart, name="cart"), 
#path('menu/<str:name>/', views.menu_details, name="menu_details"),
path'category/<str:name>/', views.menu_details, name="menu_details"),

]
