from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
    
    
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        errors = {}

        if not username:
            errors["username"] = "Введите имя пользователя"
        if not password:
            errors["password"] = "Введите пароль"

        # Проверка уникальности
        if username:
            try:
                User.objects.get(username=username)
                errors["username_exists"] = "Пользователь уже существует"
            except User.DoesNotExist:
                pass

        if errors:
            return render(request, 'registration.html', {
                'form': {
                    'username': username,
                    'email': email,
                    'errors': errors
                }
            })
        else:
            User.objects.create_user(username, email, password)
            return redirect('login')

    return render(request, 'registration.html', {'form': {}})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        errors = {}

        if not username:
            errors["username"] = "Введите логин"
        if not password:
            errors["password"] = "Введите пароль"

        user = authenticate(username=username, password=password)

        if user is None:
            errors["auth"] = "Неверный логин или пароль"

        if errors:
            return render(request, 'login.html', {
                'form': {
                    'username': username,
                    'errors': errors
                }
            })
        else:
            login(request, user)
            return redirect('archive')

    return render(request, 'login.html', {'form': {}})