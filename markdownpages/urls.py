from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.root,name='root'),
    url(r'^(?P<markdown_path>.+/)$',views.index,name='index'),
    url(r'^(?P<markdown_path>.+[^/])$',views.page,name='page'),
]
