from django.urls import  path
from hexlet_django_blog.article import  views
# from hexlet_django_blog.urls import urlpatterns
app_name = 'myapp'
urlpatterns = [
    path("<str:tags>/<int:article_id>/", views.ArticleView.as_view(), name='art1'),
    path("", views.ArticleView.as_view()),
]
