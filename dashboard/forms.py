from django.forms import ModelForm
from .models import Product, Branch

class ProductRegistrationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'price']