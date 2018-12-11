from rest_framework import serializers

from backweb.models import Art


class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        #序列化的模型
        model = Art
        #需要序列化的字段
        fields = ['title','desc','content','id']

