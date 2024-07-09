from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_in_stock, CategoryListView  # home,contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts')
    path('catalog/create/', ProductCreateView.as_view(), name='catalog_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='catalog_delete'),
    path('', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='one_product'),
    path('activity/<int:pk>/delete/', toggle_in_stock, name='toggle_in_stock'),
    path('categories/', CategoryListView.as_view(), name='categories_list')
]

