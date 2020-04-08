from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Scent, Power
from .forms import WaftingForm


# views-----------

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def scents_index(request):
    scents = Scent.objects.all()
    return render(request, 'scents/index.html', {'scents': scents})


def scents_detail(request, scent_id):
    scent = Scent.objects.get(id=scent_id)
    # powers_scent_doesnt_have = Power.object.exclude(
    #     id_in=scent.powers.all().values_list('id'))
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


class PowerList(ListView):
    model = Power


class PowerDetail(DetailView):
    model = Power


class PowerUpdate(UpdateView):
    model = Power
    fields = ['name', 'description']


class PowerDelete(DeleteView):
    model = Power
    success_url = '/powers/'
