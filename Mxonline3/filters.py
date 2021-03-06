# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Q
from goods.models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):

    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(field_name='top_category',method='top_category_filter')
    def top_category_filter(self,queryset,name,value):
        queryset = queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
        return queryset
    class Meta:
        model = Goods
        fields = ['price_min', 'price_max','name','is_hot']

