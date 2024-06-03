from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView #home,contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts')
    path('', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='one_product')
]

