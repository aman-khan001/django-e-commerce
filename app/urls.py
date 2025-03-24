from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),

    
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('details/<int:id>/', views.ProductDetails.as_view(), name="details"),
    path('profile/', views.profile, name='profile'),

    path('shoes/<slug:data>', views.shoes, name="shoes"),
    path('search/', views.search, name="search"),

    path('add-to-carts/', views.addToCart, name="addCart"),
    path('carts/', views.carts, name="carts"),
    
    path('buynow/', views.buynow, name="buynow"),
    path('checkout/', views.checkout, name="checkout"),

    path('registration/', views.RegistrationView.as_view(), name="registration"),
]

