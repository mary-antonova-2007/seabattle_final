from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, ShopCart, ShopCartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authorization.models import Profile


# Create your views here.
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    shop_cart, created = ShopCart.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = ShopCartItem.objects.get_or_create(shop_cart=shop_cart, product=product)

        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        messages.success(request, f'"{product.name}" добавлен в корзину!')

    return redirect('main')  # Предполагается, что у вас есть URL с именем 'product_list'


@login_required
def shop_cart(request):
    context = dict()
    cart = ShopCart.objects.filter(user=request.user)[0]
    context['cart_items'] = ShopCartItem.objects.filter(shop_cart=cart)
    total_summ = 0
    for item in ShopCartItem.objects.filter(shop_cart=cart):
        total_summ += item.total_price()
    context['sum_product_price'] = total_summ
    return render(request, 'store/shop_cart.html', context=context)
