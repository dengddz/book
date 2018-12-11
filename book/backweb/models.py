from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

class Art(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    keyword = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    is_display = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'


class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    is_display = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notice'

