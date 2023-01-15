from .models import feedback
from django.forms import ModelForm, TextInput

class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'number', 'telegram', 'message', 'summ']

        widgets = {
            'name': TextInput(attrs={
                'class': 'wLine',
                 'placeholder': 'Ваше имя'
            }),
            'number': TextInput(attrs={
                'class': 'wLine',
                'placeholder': 'Номер телефона'
            }),
            'telegram': TextInput(attrs={
                'class': 'wLine',
                'placeholder': '@nickname'
            }),
            'summ': TextInput(attrs={
                'class': 'wLine',
                'placeholder': 'Сумма обмена'
            }),
            'message': TextInput(attrs={
                'class': 'wLine',
                'placeholder': 'Коментарий'
            })
        }