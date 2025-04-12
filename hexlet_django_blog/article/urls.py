from django.urls import  path
from hexlet_django_blog.article import  views
# from hexlet_django_blog.urls import urlpatterns

urlpatterns = [
    path("", views.index)
]