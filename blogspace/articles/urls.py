from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    re_path('^$', views.article_list, name='list'),
    re_path('^create/$', views.article_create, name='create'),
    # Slug can be with any len of alphnum or -
    # Url param capturing using ?P<>
    re_path('^(?P<slug>[\w-]+)/$', views.article_detail, name='detail')
]
