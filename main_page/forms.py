from django import forms
from django.forms.widgets import TextInput, PasswordInput

from . import models as m


class LoginForm(forms.ModelForm):

    class Meta:
        model = m.User
        fields = ['email', 'password']
        widgets = {
            'email': TextInput(attrs={
                'class': 'log-in__input',
                'placeholder': 'Электронная почта',
                'name': 'name',
                'id': 'name',
                'type': 'text',
            }),
            'password': PasswordInput(attrs={
                'class': 'log-in__input',
                'placeholder': 'Пароль',
                'name': 'password',
                'id': 'password',
                'type': 'password',
            }),
        }
