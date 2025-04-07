from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from website.forms import SignUpForm


def index(request):
    date = datetime.today()
    return render(request, 'website/index.html', context={'today':date})

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