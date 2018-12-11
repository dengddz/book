from rest_framework import filters
import django_filters
from backweb.models import Art


class ArtFilter(filters.FilterSet):
    #过滤URL中的title
    title = django_filters.CharFilter('title',lookup_expr='contains')
    #过滤desc参数
    dasc = django_filters.CharFilter('dasc',lookup_expr='contains')
    content = django_filters.CharFilter('content',lookup_expr='contains')
    #过滤时间最小值min_time
    min_time = django_filters.DateTimeFilter('ctrate_time',lookup_expr='gt')
    #过滤时间最大值
    max_time = django_filters.DateTimeFilter('ctrate_time',lookup_expr='lt')

    class Meta:
        model = Art
        fields = ['title','dasc','content']