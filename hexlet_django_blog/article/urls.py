from django.urls import  path
from hexlet_django_blog.article import  views
from hexlet_django_blog.article.views import IndexView, ArticleView2, ArticleFormEditView, ArticleFormDeleteView
# from hexlet_django_blog.urls import urlpatterns
app_name = 'myapp'
urlpatterns = [
    path("<str:tags>/<int:article_id>/", views.ArticleView.as_view(), name='art1'),
    path("<int:article_id>/edit/", ArticleFormEditView.as_view(), name='edit_article'),
    path("<int:article_id>/delete/", ArticleFormDeleteView.as_view(), name='delete_article'),
    path("<int:article_id>/", ArticleView2.as_view(), name='one_article'),
    path("", IndexView.as_view(), name='article_list'),
    path("create/", views.ArticleFormCreateView.as_view(), name='cr_art'),
]

