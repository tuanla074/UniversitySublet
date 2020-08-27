import django_filters
from django import forms
from django_filters import NumberFilter, DateTimeFilter, DateFilter
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class SubletFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="sublet_start_date", lookup_expr='gte', label=' start date',
                                widget=DateInput({'type': 'date'}))
    end_date = DateTimeFilter(field_name="sublet_end_date", lookup_expr='lte', label='end date',
                              widget=DateInput({'type': 'date'}))
    price = NumberFilter(field_name="sublist_price", lookup_expr='lte', label='max rent')

    class Meta:
        model = SubletListing
        fields = '__all__'
        exclude = ['sublet_owner_info', 'total_room', 'utilities',
                   'sublet_legal_fee', 'parking_cost', 'sublet_status',
                   'room_number', 'sublet_start_date', 'sublet_end_date', 'sublist_price']
