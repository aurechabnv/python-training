from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from website.forms import SignUpForm


# CBV: class-based view
class HomeView(TemplateView):
    template_name = "website/index.html"
    title = "Default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["today"] = datetime.today()
        return context

# FBV: function-based view
def index(request):
    date = datetime.today()
    return render(request, 'website/index.html', context={'today':date, 'title':'Bienvenue sur mon site'})

def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse("Merci de vous être inscrit au site")

    return render(request, 'accounts/signup.html', context={'form': form})