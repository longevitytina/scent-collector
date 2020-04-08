from django.shortcuts import render, redirect
from .models import Scent
from django.http import HttpResponse
from .forms import WaftingForm


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
    wafting_form = WaftingForm()
    return render(request, 'scents/detail.html', {'scent': scent, 'wafting_form': wafting_form})


def add_emotion(request, scent_id):
    form = WaftingForm(request.POST)
  # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the scent_id assigned
        new_emotion = form.save(commit=False)
        new_emotion.scent_id = scent_id
        new_emotion.save()
    return redirect('detail', scent_id=scent_id)
