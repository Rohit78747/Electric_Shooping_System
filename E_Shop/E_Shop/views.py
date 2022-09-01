from django.shortcuts import redirect,render
from store_app.models import Product

def Base(request):
    return render(request,'main/base.html')

def Home(request):
    product = Product.objects.filter(status='Publish')

    context={
        'product':product
    }

    return render(request, 'main/index.html',context)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')

    context = {
        'product': product
    }
    return render(request, 'main/product.html',context)