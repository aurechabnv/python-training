from datetime import datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, 'DjangoExample/index.html', context={'today':date})