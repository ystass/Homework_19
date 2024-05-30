from django.shortcuts import render, get_object_or_404

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


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def one_product(request, pk):
    product_one = get_object_or_404(Product, pk=pk)#Product.objects.get(pk=pk)
    context = {'product': product_one}
    return render(request, 'product_one.html', context)
