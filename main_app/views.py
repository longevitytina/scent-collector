from django.shortcuts import render
from .models import Scent
from django.http import HttpResponse


# views-----------

def home(request):
    return HttpResponse('<h1>Scent Collector (✿ヘᴥヘ)</h1>')


def about(request):
    return render(request, 'about.html')


def scents_index(request):
    scents = Scent.objects.all()
    return render(request, 'scents/index.html', {'scents': scents})
