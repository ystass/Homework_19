from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


# def home(request):
#     return render(request, 'home.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#     return render(request, 'contacts.html')
class ProductListView(ListView):
    model = Product




# def product(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    #


# def one_product(request, pk):
#     product_one = get_object_or_404(Product, pk=pk)#Product.objects.get(pk=pk)
#     context = {'product': product_one}
#     return render(request, 'product_detail.html', context)
