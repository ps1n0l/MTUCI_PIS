from django.contrib import admin
from django.urls import path, re_path
from articles.views import archive, get_article, create_post

urlpatterns = [
    path('', archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)$', get_article, name='get_article'),
    path('article/new/', create_post, name='create_post'),
    path('admin/', admin.site.urls),
]
