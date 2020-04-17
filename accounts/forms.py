from django.forms import ModelForm
from .models import Order, Customer

from django.contrib.auth.models import User


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
