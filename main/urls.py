from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('add_basket', views.add_basket, name='add_basket'),
    path('registration', views.registration, name='registration'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('buy', views.buy, name='buy')
]