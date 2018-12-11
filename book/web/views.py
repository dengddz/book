from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from backweb.models import Art


# Create your views here.
from web.art_ser import ArticleSerializer


def index(request):
    if request.method == 'GET':
        return render(request, 'web/index.html')
    if request.method == 'POST':
        pass

def list(request):
    if request.method == 'GET':
        return render(request,'web/list.html')
    if request.method == 'POST':
        pass

def share(request):
    if request.method == 'GET':
        return render(request,'web/article.html')
    if request.method == 'POST':
        pass

def gbook(request):
    if request.method == 'GET':
        return render(request,'web/gbook.html')


def about(request):
    if request.method == 'GET':
        return render(request,'web/about.html')
    if request.method == 'POST':
        pass

def info(request):
    if request.method == 'GET':
        return render(request,'web/info.html')
    if request.method == 'POST':
        pass

class ArticleView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):

    queryset = Art.objects.all()
    #序列化返回的文章
    serializer_class = ArticleSerializer
    #过滤
    # filter_class = ArtFilter
    #
    # def perform_destroy(self, instance):
    #     instance.is_delete = 1
    #     print('111')
    #     instance.save()

    # def get_queryset(self):
        # search_title = self.request.GET.get('title')
        # search_content = self.request.GET.get('content')
        # return self.queryset.filter(title__contains=search_title,content__contains= search_content)

    # def retrieve(self, request, *args, **kwargs):
    #     data = {
    #         'code':200,
    #         'msg':'请求成功'
    #     }
    #     try:
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance)
    #         return Response(serializer.data)
    #     except:
    #         data['code'] = 500
    #         data['msg'] = '获取数据失败'
    #         return Response(data)