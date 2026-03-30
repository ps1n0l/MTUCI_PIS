from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all()  # получаем все статьи из БД
    return render(request, 'archive.html', {'posts': posts})