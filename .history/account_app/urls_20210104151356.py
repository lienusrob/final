from django.urls import path, include
from .views import HomeView, SignUp #UserListView, UserDetailView
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    # path ('', HomeView.as_view(), name = 'homepage'),
    #path('signup', SignUp.as_view(template_name = 'registration/signup.html'), name='signup'),
   # path('login', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(next_page = 'homepage'), name = 'logout'),
    path('register', views.user_register, name='user_register'),
    path('login/',views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    #path ('profile/', UserDetailView.as_view(template_name = 'registration/profile.html'), name= 'profile'),

]
