from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views import View

from hexlet_django_blog.article.models import Article

class ArticleView(TemplateView):
    template_name = 'article/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticleView2(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(
            request,
            "article/detail.html",
            context={'article': article}
        )

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "article/index.html",
            context={'articles': articles}
        )

# def index(request):
#     # return HttpResponse('article')
#     return render(request, 'article/index.html')