from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product, one_product #home,contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts')
    path('', product, name='product'),
    path('product/<int:pk>/', one_product, name='one_product')
]

