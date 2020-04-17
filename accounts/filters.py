from django_filters import FilterSet
from .models import Order


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['ordered_customer', 'date_created']
