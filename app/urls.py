from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('product-detail/', views.product_details, name="product-detail"),
    path('cart/', views.add_to_cart, name="cart"),
    path('buy/', views.buy_now, name="buy-now"),
    path('profile/', views.profile, name="profile"),
    path('address/', views.address, name="address"),
    path('orders/', views.orders, name="orders"),
    path('changepassword/', views.change_password, name="change-password"),
    path('mobile/', views.mobile, name="mobile"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('checkout/', views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_url = settings.MEDIA_ROOT)

