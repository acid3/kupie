from django import forms
from .models import ProductBase

class addProductForm(forms.ModelForm):
    class Meta():
        model = ProductBase
        fields = ['title', 'category', 'text', 'from_state', 'from_city', 'price']
