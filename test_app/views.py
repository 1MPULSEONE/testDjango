from django.http import HttpResponseNotFound
from django.shortcuts import render

from test_app.models import Article

articles = [
    {
        'id': 1,
        'title': 'First news',
        'text': 'This is the worst article'
    },
    {
        'id': 2,
        'title': 'Second news',
        'text': 'This is the amazing second article'
    }]


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'test_app/news_list.html', {'articles': articles})


def about(request):
    return render(request, 'test_app/about.html')


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'test_app/news_article.html', {'article': article})
