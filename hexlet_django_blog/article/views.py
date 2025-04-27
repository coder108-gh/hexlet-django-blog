from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views import View
from .forms import ArticleForm
from django.contrib import messages
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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SUCCESS!!!')
            return redirect('art:article_list')
        messages.error(request, 'ERROR!')
        return render(request, 'article/create.html', {'form': form})

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        art_id = kwargs.get('article_id')
        article = Article.objects.get(id=art_id)
        form = ArticleForm(instance=article)
        return render(request,'article/update.html',{'form': form, 'article_id': art_id})

    def post(self, request, *args, **kwargs):
        art_id = kwargs.get('article_id')
        article = Article.objects.get(id=art_id)
        form = ArticleForm(request.POST,  instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'UPDATED')
            return redirect('art:article_list')

        messages.error(request, 'ERROR!')
        return render(request, 'article/update.html',{'form': form, 'article_id': art_id})

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        art_id = kwargs.get('article_id')
        article = Article.objects.get(id=art_id)
        if article:
            article.delete()
            messages.success(request, 'deleted!')
        return redirect('art:article_list')