from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
       products = Product.objects.all()
       return render(request, 'shop/index.html', {'products': products})

# def members(request):
#     return HttpResponse(request, "submitform.html")

def about(request):
    template = loader.get_template('shop/submitform.html')
    return HttpResponse(template.render())