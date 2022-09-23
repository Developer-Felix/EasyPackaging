from owner.views import admin_index

from django.urls import path

app_name = 'owner'

urlpatterns = [
    path('', admin_index,name='admin-index-page'),

]