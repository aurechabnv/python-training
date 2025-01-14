from django.urls import path

from .views import index, article, blog_post

urlpatterns = [
    path('', index, name='blog-index'),
    path('article_<str:numero_article>/', article, name='blog-article'),
    path('<str:slug>/', blog_post, name='blog-post'),
]
