from datetime import date

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost
from website.forms import BlogPostForm



# CLASS-BASED VIEWS
class BlogIndexView(ListView):
    model = BlogPost
    # or
    # queryset = BlogPost.objects.filter(published=True)

    template_name = 'blog/index.html'
    context_object_name = 'posts'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/new.html'
    # fields = ['title', 'content']
    # or
    form_class = BlogPostForm
    success_url = reverse_lazy("blog-index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Créer'
        return context

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/new.html'
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Modifier'
        return context

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete.html'
    success_url = reverse_lazy("blog-index")


# FUNCTION-BASED VIEWS
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
    response = render(request, 'blog/post.html', context={'blogpost': post})
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
        return HttpResponseRedirect(reverse('blog-index'))
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = date.today()
        form = BlogPostForm(initial=init_values)

    return render(request, "blog/new.html", {"form": form})
