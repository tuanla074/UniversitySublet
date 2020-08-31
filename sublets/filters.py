import django_filters
from django import forms
from django.forms import NumberInput
from django_filters import NumberFilter, DateTimeFilter, DateFilter, ChoiceFilter
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class SubletFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="start_date_search", lookup_expr='gte', label=' start subletting date',
                                widget=DateInput({'type': 'date', 'class': 'sp'}))
    end_date = DateTimeFilter(field_name="end_date_search", lookup_expr='lte', label='end subletting date',
                              widget=DateInput({'type': 'date', 'class': 'sp'}))
    price = NumberFilter(field_name="sublist_price", lookup_expr='lte', label='max rent',
                         widget=NumberInput({'class': 'sp'}))
    min_price = NumberFilter(field_name="sublist_price", lookup_expr='gte', label='min rent',
                         widget=NumberInput({'class': 'sp'}))

    class Meta:
        model = SubletListing
        fields = '__all__'
        exclude = ['sublet_owner_info', 'total_room', 'utilities',
                   'sublet_legal_fee', 'parking_cost', 'sublet_status',
                   'room_number', 'sublet_start_date', 'sublet_end_date', 'sublist_price',
                   'start_date_search', 'end_date_search', 'sublet_main_image', 'sublet_description']
