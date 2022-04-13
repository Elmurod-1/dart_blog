from django.shortcuts import render
from .models import Article, Category


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        }
    return render(request, template_name='blog/index.html', context=context)

def single(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/single.html', context={'article': article})