from django.urls import path

from .views import index, article, blog_post, new_post

urlpatterns = [
    path('', index, name='blog-index'),
    path('new/', new_post, name='new-post'),
    path('article_<str:numero_article>/', article, name='blog-article'),
    path('<str:slug>/', blog_post, name='blog-post'),
]
