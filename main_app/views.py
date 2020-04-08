from django.shortcuts import render, redirect
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


def scents_detail(request, scent_id):
    scent = Scent.objects.get(id=scent_id)
    return render(request, 'scents/detail.html', {'scent': scent})
