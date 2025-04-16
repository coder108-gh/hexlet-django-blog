from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

class ArticleView(TemplateView):
    template_name = 'article/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# def index(request):
#     # return HttpResponse('article')
#     return render(request, 'article/index.html')