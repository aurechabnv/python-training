from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from blog.models import BlogPost


@user_passes_test(lambda u: u.username == 'doare')
def index(request):
    posts = BlogPost.objects.all()
    # posts = BlogPost.objects.filter(pk__in=[1,2,3])
    return render(request, 'blog/index.html', context={'posts': posts})
    # return redirect('home')

def article(request, numero_article):
    if numero_article in ['01', '02', '03']:
        return render(request, f'blog/article_{numero_article}.html')
    return render(request, 'blog/article_not_found.html')

def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    # response = HttpResponse(render_to_string('blog/post.html', context={'blog_post': post}))
    response = render(request, 'blog/post.html', context={'blog_post': post})
    return response
