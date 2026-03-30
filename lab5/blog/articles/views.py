from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.all()  # получаем все статьи из БД
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):
    if not request.user.is_authenticated:
        raise Http404("Только авторизованные пользователи могут создавать статьи.")

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()
        errors = {}

        if not title:
            errors["title"] = "Пожалуйста, укажите название статьи."
        if not text:
            errors["text"] = "Пожалуйста, введите текст статьи."

        # Проверка уникальности названия 
        if title and Article.objects.filter(title=title).exists():
            errors["title_unique"] = "Статья с таким названием уже существует."

        if errors:
            return render(request, 'create_post.html', {
                'form': {'title': title, 'text': text, 'errors': errors}
            })
        else:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            # Перенаправляем на страницу созданной статьи
            return redirect('get_article', article_id=article.id)
    else:
        # GET-запрос – показать пустую форму
        return render(request, 'create_post.html', {'form': {}})