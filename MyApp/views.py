from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from MyApp.models import Product, Catergory, CartOder, CartOderItems,ProductImages, Vendor, order_img

def index(request):
    products = Product.objects.all()

    context = {
        "products":products
    }

    return render(request, 'app/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products":products
    }

    return render(request, 'app/product-list.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    p_image = product.p_images.all()

    context = {
        "product": product,
        "p_image": p_image,
    }
    return render(request, "app/product-detail.html", context)
# Create your views here.

# def add_to_cart(request):
#     cart_product = {}

#     cart_product[str(request.GET['id'])] = {
#         'title': request.GET['title'],
#         'price': request.GET['price'],
#     }
#     if 'cart_data_obj' in request.session:
#         if str(request.GET[id]) in request.session['cart_data_obj']:
#             cart_data = request.session['cart_data_obj']
#             cart_data.update(cart_data)
#             request.session['cart_data_obj'] = cart_data
#     return JsonResponse({"data": request.session['cart_data_obj'], 'totalcartitems'})

    # if 'cart_data_obj' in request.session:
    #     if str(request.GET[id]) in request.session['cart_data_obj']:
    #         cart_data = request.session['cart_data_obj']
    #         cart_data[str(request.GET['id'])][]

#     '''**********detailProdactView *************

# def product_detail_view(request,pid):
#     product = Product.objects.get(pid=pid)
#     products = Product.objects.filter(category=product.category.exclude(pid=pid)

#     p_image = product.p_images.all()

#     context = {
#         "p" : product,
#         "p_image" : p_image,
#         "products" :products,
#     }
#     return render(request, "app/product_detail.html", context)
    


# '''