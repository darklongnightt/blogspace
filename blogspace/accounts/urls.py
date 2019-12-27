from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path('^register/$', views.register_view, name='register'),
    re_path('^login/$', views.login_view, name='login'),
    re_path('^logout/$', views.logout_view, name='logout')
]
