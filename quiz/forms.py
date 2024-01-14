from django import forms
from .models import Ship, Product

class ShipCreationForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = ['battlefield', 'prize', 'horizontal_index', 'vertical_index']

    def __init__(self, *args, **kwargs):
        super(ShipCreationForm, self).__init__(*args, **kwargs)

        # Здесь можно добавить дополнительную логику инициализации, например:
        # Установить начальный выбор или ограничить выбор товаров
        self.fields['prize'].queryset = Product.objects.all()

        # Можно также настроить виджеты для полей, если нужно
        self.fields['horizontal_index'].widget = forms.NumberInput(attrs={'min': 0})
        self.fields['vertical_index'].widget = forms.NumberInput(attrs={'min': 0})