from django.conf.urls import url

from backweb import views

urlpatterns = [
    url(r'^login/', views.login,name='login'),
    url(r'^rejister/', views.rejister,name='rej'),
    url(r'^index',views.index,name='index'),
    url(r'^article/',views.article,name='article'),
    url(r'^notice/',views.notice,name='notice'),
    url(r'^comment/',views.comment,name='comment'),
    url(r'^add_art/',views.add_art,name='add_art'),
    url(r'^update_art/',views.update_art,name='update_art'),
    url(r'^delete_art/',views.delete_art,name='delete_art'),
    url(r'^add_notice/', views.add_notice, name='add_notice'),
    url(r'^delete_notice/',views.delete_notice, name='delete_notice')

]