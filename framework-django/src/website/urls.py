"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website.views import HomeView
from .views import index, signup

urlpatterns = [
    path('', HomeView.as_view(title="Bienvenue sur mon site"), name='home'),
    path('about/', HomeView.as_view(title="A propos"), name='about'),
    path('signup/', signup, name='signup'),
    path('backend/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
