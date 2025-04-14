from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('article')
    return render(request, 'article/index.html')