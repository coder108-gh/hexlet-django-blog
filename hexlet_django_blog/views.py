from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import View


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'My World'
        return context

    def get(self, request, *args, **kwargs):
        return redirect(reverse('art:art1',kwargs={'tags': 'go', 'article_id': 777}))

# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={'who': 'World'}
#     )

def about(request):
    return render(request, "about.html")

