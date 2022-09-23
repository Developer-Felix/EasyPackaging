from products.views import index,products_detail,orders

from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', index,name='index-page'),
    path('product/order/', orders,name='order-page'),
    path('product/', products_detail,name='products-detail-page'),
]