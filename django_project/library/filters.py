import django_filters
from django_filters import CharFilter

from .models import *

class AuthorFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'races', 'gender',
        'non_marginalized', 'uses_ownvoice', 'is_immigrant', 'is_neurodiverse',
        'is_disabled', 'is_lgbtqia']

class BookFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['notes', 'characters']

# TODO In the future, a character search functionality is desired.