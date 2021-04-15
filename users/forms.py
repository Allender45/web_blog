from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, label='Введите логин',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    email = forms.EmailField(required=True, label='Введите емайл',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, label='Введите пароль', help_text='Не меньше 8 символов.',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль' }))
    password2 = forms.CharField(required=True, label='Повторите пароль', help_text='Должен совпадать с паролем.',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
