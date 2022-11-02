from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request,'commontemp/index.html')

def common_cart(request):
    return render(request,'commontemp/cart.html')
   