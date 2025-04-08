from django.urls import path

from .views import article, blog_post, new_post, BlogIndexView, BlogPostDetailView, BlogPostCreateView, \
    BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogIndexView.as_view(), name='blog-index'),
    path('new/', BlogPostCreateView.as_view(), name='new-post'),
    path('article_<str:numero_article>/', article, name='blog-article'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='blog-post'),
    path('<str:slug>/edit/', BlogPostUpdateView.as_view(), name='blog-post-edit'),
    path('<str:slug>/delete/', BlogPostDeleteView.as_view(), name='blog-post-delete'),
]
