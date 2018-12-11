from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from backweb.Artform import AddArtForm, AddNotForm
from backweb.models import User, Art, Notice
from django.urls import reverse

def login(request):
    if request.method == 'GET':
        return render(request,'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(username=username).first()
        if user:
            if user.password == password:
                return HttpResponseRedirect('/backweb/index/')
            else:
                err = '密码错误'
                return render(request,'backweb/login.html',{'err':err})
        else:
            err2 = '账号错误'
            return render(request,'backweb/login.html',{'err':err2})

def rejister(request):
    if request.method == 'GET':
        return render(request,'backweb/rejister.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if username and password and password2:
            user = User.objects.filter(username=username).first()
            if user:
                err3 = '该用户名已经被注册'
                return render(request,'backweb/rejister.html',{'err':err3})
            if password == password2:
                a = '注册成功'
                User.objects.create(username=username,password=password)
                return render(request, 'backweb/rejister.html', {'err': a})
            else:
                err4 = '前后密码不一致'
                return render(request, 'backweb/rejister.html', {'err': err4})
        else:
            err5 = '内容不能为空'
            return render(request, 'backweb/rejister.html', {'err': err5})


def index(request):
    if request.method == 'GET':
        return render(request,'backweb/index.html')
    # if request.method == 'POST':
    #     return HttpResponseRedirect(reversed('backweb:comment'))

def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        articles = Art.objects.all()
        paginator = Paginator(articles, 2)
        page = paginator.page(page)
        return render(request,'backweb/article.html',{'page': page})


def notice(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Notice.objects.all()
        paginator = Paginator(articles, 2)
        page = paginator.page(page)

        return render(request,'backweb/notice.html', {'page': page})


def comment(request):
    if request.method == 'GET':
        return render(request,'backweb/comment.html')
    if request.method == 'POST':
        pass

def add_art(request):
    if request.method == 'GET':
        return render(request,'backweb/add-article.html')
    if request.method == 'POST':
        form = AddArtForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            keyword = form.cleaned_data['keyword']
            is_display = form.cleaned_data['is_display']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Art.objects.create(title=title,desc=desc,keyword=keyword,content=content,icon=icon,is_display=is_display )
            return HttpResponseRedirect('/backweb/article/')
        else:
            return render(request,'backweb/add-article.html',{'form':form})


def update_art(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        article = Art.objects.filter(pk=id).first()
        return render(request,'backweb/update-article.html',{'article': article})
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            # 验证成功
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            keyword = form.cleaned_data['keyword']
            is_display = form.cleaned_data['is_display']
            print(title,desc,content)
            id = request.GET.get('id')
            article = Art.objects.filter(pk=id).first()
            article.title = title
            article.keyword = keyword
            article.desc = desc
            article.content = content
            article.is_display = is_display
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            # 验证失败
            article = Art.objects.filter(pk=id).first()
            return render(request,'backweb/update-article.html',
                          {'form': form, 'article': article})





def delete_art(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        Art.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def add_notice(request):
    if request.method == 'GET':
        return render(request,'backweb/add-notice.html')
    if request.method == 'POST':
        form = AddNotForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            is_display = form.cleaned_data['is_display']
            Notice.objects.create(title=title,content=content,icon=icon,is_display=is_display )
            return HttpResponseRedirect('/backweb/notice/')
        else:
            return render(request,'backweb/add-notice.html',{'form':form})

def delete_notice(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        Notice.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:notice'))