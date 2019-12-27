from django.contrib import admin
from django.urls import path, re_path, include
from . import views
# Allows django to define where static files are
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings

# Use re_path in future for regex matchings
urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^articles/', include('articles.urls')),
    re_path('^accounts/', include('accounts.urls')),
    re_path('^about/$', views.about),
    re_path('^$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
