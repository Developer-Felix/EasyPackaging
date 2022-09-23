from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home',
        'content': 'Hello World',
    }
    return render(request, "pages/index.html",data)

def products_detail(request):
    data = {
        'title': 'Product',
        'content': 'Hello World',
    }
    return render(request, "pages/product_detail.html", data)

def orders(request):
    data = {
        'title': 'Make Order',
        'content': 'Hello World',
    }
    return render(request, "pages/order.html", data)
