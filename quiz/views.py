from django.shortcuts import render, redirect
from .models import BattleField, Ship
from store.models import Product
from django.contrib.auth.decorators import login_required
from .forms import ShipCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def play_quiz(request):
    pass


def create_battlefield(request, user_id):
    pass


def edit_battlefield(request, battlefield_id):
    referer_url = request.META.get('HTTP_REFERER')
    battlefield = BattleField.objects.get(id=battlefield_id)
    context = dict()

    ships = Ship.objects.filter(battlefield__isnull=True)
    context['products'] = Product.objects.all()

    context['battlefields'] = BattleField.objects.all()
    context['battlefield'] = battlefield
    context['ships'] = ships
    context['horizontal_indexes'] = range(battlefield.horizontal_size)
    context['vertical_indexes'] = range(battlefield.vertical_size)
    context['ship_create_form'] = ShipCreationForm()

    if request.method == 'POST':
        form_type = request.POST.get('form-type')
        if form_type == 'ship_creation':
            ship_create_form = ShipCreationForm(request.POST)
            if ship_create_form.is_valid():
                ship = ship_create_form.save(commit=False)
                ship.save()
                if referer_url:
                    return HttpResponseRedirect(referer_url)
                else:
                    return redirect('main')
            else:
                # Если форма не прошла валидацию, передаем её обратно в контекст с ошибками
                context['ship_create_form'] = ship_create_form
                return render(request, 'quiz/edit_battlefield.html', context)

    print(ships)
    return render(request, 'quiz\edit_battlefield.html', context=context)


@login_required
def create_ship(request):
    if request.method == 'POST':
        form = ShipCreationForm(request.POST)
        if form.is_valid():
            # Создаем корабль на основе валидных данных
            ship = form.save(commit=False)
            ship.battlefield = BattleField.objects.get(user=request.user)  # Получаем поле пользователя
            ship.save()
            return redirect('some_view_name')  # Перенаправляем пользователя после создания корабля
    else:
        form = ShipCreationForm()

    products = Product.objects.all()  # Получаем список товаров для отображения в форме
    ships = Ship.objects.filter(battlefield__user=request.user)  # Получаем список кораблей пользователя
    context = {
        'form': form,
        'products': products,
        'ships': ships,
    }
    return render(request, 'your_template_name.html', context)
