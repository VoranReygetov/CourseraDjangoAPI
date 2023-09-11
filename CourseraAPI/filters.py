import django_filters
from .models import *

class YourModelFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'field1': ['exact', 'contains'],
            'field2': ['exact', 'icontains'],

        }