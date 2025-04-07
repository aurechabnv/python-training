from datetime import date

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from blog.models import BlogPost
from website.forms import BlogPostForm


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

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # blog_post = form.save(commit=False)
            # blog_post.published = True
            # blog_post.save()
        return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = date.today()
        form = BlogPostForm(initial=init_values)

    return render(request, "blog/new.html", {"form": form})
