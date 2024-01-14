from django.shortcuts import render
from store.models import Product, ShopCart, ShopCartItem
from django.contrib.auth.models import User
from quiz.models import BattleField


def get_users_without_battlefield():
    return User.objects.filter(battlefield=None)


def main(request):
    total_price = 0
    total_items = 0
    context = dict()
    context['products'] = Product.objects.all()

    if request.user.is_authenticated:
        if request.user.is_superuser:
            context['battlefields'] = BattleField.objects.all()
        carts = ShopCart.objects.filter(user=request.user)
        if len(carts) < 1:
            cart = ShopCart(user=request.user)
            cart.save()
        else:
            cart = carts[0]
        for cart_item in ShopCartItem.objects.filter(shop_cart=cart):
            total_price += cart_item.product.price * cart_item.quantity
            total_items += 1
        context['total_price'] = total_price
        context['total_items'] = total_items
    return render(request, 'main.html', context=context)
