from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import (
    Customer,
    Product,
    Cart,
    OrederPlaced
)

class ProductView(View):
    def get(self, request):
        camera = Product.objects.filter(category='C')
        sunglasses = Product.objects.filter(category='S')
        shoes = Product.objects.filter(category='Sh')
        context = {
            'camera': camera,
            'shoes': shoes,
            'sunglasses': sunglasses
        }
        
        return render(request, 'index.html', context)

class ProductDetails(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, 'productDetails.html', {'product': product})

def shoes(request, data=None):
    if data == 'None':
        products = Product.objects.filter(category='Sh')
    elif data == 'campus':
        products = Product.objects.filter(category='Sh').filter(brand = 'Campus')
    elif data == 'Nike':
        products = Product.objects.filter(category='Sh').filter(brand = 'Nike')

    elif data == 'below':
        products = Product.objects.filter(category='Sh').filter(discounted_price__lt = 50)

    elif data == 'above':
        products = Product.objects.filter(category='Sh').filter(discounted_price__gt = 49)
    return render(request, 'shoes.html', {'products': products})

def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains = q)
    return render(request, 'search.html', {'data':data, 'q': q})


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation! Registered Successfully')
            form.save()
        return render(request, 'registration.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')

def addToCart(request):
    user = request.user
    product_id = request.GET.get('pro_id')
    product = Product.objects.get(pk = product_id)
  
    for user in User.objects.all():
        Customer.objects.get_or_create(user=user)
    customer = Customer.objects.get(user=user)
    Cart(user=customer, product=product).save()
    return render(request, 'carts.html')



def carts(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart = Cart.objects.filter(user = customer)

    total_price = 0
    for i in cart:
        total_price += i.product.discounted_price * i.quantity

    return render(request, 'carts.html', {'carts': cart, 'total':total_price})


def buynow(request):
    return render(request, 'buynow.html')


def checkout(request):
    return render(request, 'checkout.html')



