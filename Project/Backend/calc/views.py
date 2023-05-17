from django.shortcuts import render
from django.http import HttpResponse

from calc.models import Product

# Create your views here.


def home(request):
        prod = Product.objects.all();
        
        return render(request,"Home.html",{'prod':prod})
