from ctypes import sizeof
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from main.models import *
from django.core.exceptions import ValidationError


class SizeForm(forms.Form):
    size = forms.CharField(
        widget=forms.NumberInput(attrs={"placeholder": "Размерность матрицы"})
    )


def check_login_exists(login):
    if User.objects.filter(username=login).exists():
        raise ValidationError("Такой пользователь уже существует")


class LoginForm(forms.Form):  # форма авторизации и аутентификации
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    login.widget.attrs.update({"class": "form-control", "autocomplete": "off"})
    password.widget.attrs.update({"class": "form-control", "autocomplete": "off"})

    def clean(self):
        login = self.cleaned_data["login"]
        password = self.cleaned_data["password"]

        if not User.objects.filter(username=login).exists():
            raise ValidationError("Пользователь не существует")
        user = User.objects.get(username=login)
        if user:
            if not user.check_password(password):
                raise ValidationError("Неверный пароль")

        return self.cleaned_data


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    login = forms.EmailField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    def clean_login(self):
        new_login = self.cleaned_data["login"]
        check_login_exists(new_login)
        return new_login

    def save_user(self):
        new_user = User.objects.create(
            username=self.cleaned_data["login"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            password=make_password(self.cleaned_data["password"]),
            email=self.cleaned_data["login"],
        )
        return new_user
