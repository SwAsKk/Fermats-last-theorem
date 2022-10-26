from ctypes import sizeof
from django import forms

class SizeForm(forms.Form):
    size = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Размерность матрицы'}
        )
    )