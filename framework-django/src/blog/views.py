from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from blog.models import BlogPost


def index(request):
    # return render(request, 'blog/index.html')
    return redirect('home')

def article(request, numero_article):
    if numero_article in ['01', '02', '03']:
        return render(request, f'blog/article_{numero_article}.html')
    return render(request, 'blog/article_not_found.html')

def blog_post(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404(f"L'article '{slug}' n'existe pas")

    # response = HttpResponse(render_to_string('blog/post.html', context={'blog_post': post}))
    response = render(request, 'blog/post.html', context={'blog_post': post})
    return response
