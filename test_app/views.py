from django.shortcuts import render

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
    return render(request, 'test_app/news_list.html', {'articles': articles})


def about(request):
    return render(request, 'test_app/about.html')


def get_article(request, article_id):
    article = articles[article_id - 1]
    return render(request, 'test_app/news_article.html', {'article': articleп})
