from django.urls import path
from .import views

app_name = 'common'

urlpatterns = [
    path('', views.common_home, name = 'common_home'),
    path('cart', views.common_cart, name = 'common_cart'),
   
    
]