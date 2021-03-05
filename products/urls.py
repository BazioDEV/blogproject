from django.urls import path
from .views import create_product, list_products, update_product, delete_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_products'),
    path('delete/<int:id>/', delete_product, name='delete_products'),
]
