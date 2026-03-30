from django.contrib import admin
from django.urls import path, re_path
from articles.views import archive, get_article, create_post, register, login_view

urlpatterns = [
    path('', archive, name='archive'),
    re_path(r'^article/(?P<article_id>\d+)$', get_article, name='get_article'),
    path('article/new/', create_post, name='create_post'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
]
