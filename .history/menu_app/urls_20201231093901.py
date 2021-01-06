
# from project.account_app.views import HomeView
from django.urls import path
from . import views

urlpatterns = [

#path('', views.menu_list_view(template_name = 'menu_app/menu_list.html'), name = 'menu_list'),
path('menu/', views.menu_list_view, name = 'menu_list'),
#path ('', views.menu_category, name = 'menu_category'), 
#path ('admin_page/', views.menu_item, name = 'menu_item'),

]