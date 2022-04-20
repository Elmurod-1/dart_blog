from django.shortcuts import render, get_object_or_404
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
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'blog/single.html', context=context)