from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def product_details(request):
    return render(request, 'product-details.html')



def add_to_cart(request):
    return render(request, 'add-to-cart.html')


def buy_now(request):
    return render(request, 'buy-now.html')


def product_details(request):
    return render(request, 'product-details.html')



def profile(request):
    return render(request, 'profile.html')


def address(request):
    return render(request, 'address.html')


def orders(request):
    return render(request, 'orders.html')



def mobile(request):
    return render(request, 'mobile.html')


def change_password(request):
    return render(request, 'change-password.html')



def login(request):
    return render(request, 'login.html')


def checkout(request):
    return render(request, 'checkout.html')



def registration(request):
    return render(request, 'registration.html')

