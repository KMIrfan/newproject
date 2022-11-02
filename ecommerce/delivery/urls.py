from django.urls import path
from .import views

app_name = 'delivery'

urlpatterns = [
    path('index', views.delivery_home, name = 'deliveryhome'),
]