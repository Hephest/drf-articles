from rest_framework import generics
from django_filters import rest_framework as filters

from api.models import Article


class ArticleFilter(filters.FilterSet):
    user = filters.CharFilter()
    content = filters.CharFilter()
    created_from = filters.DateFilter(
        field_name='created',
        lookup_expr='gte'
    )
    created_to = filters.DateFilter(
        field_name='created',
        lookup_expr='lte'
    )

    class Meta:
        model = Article
        fields = ['user', 'content', 'created_from', 'created_to']
