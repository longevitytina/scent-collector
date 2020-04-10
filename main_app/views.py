from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Scent, Power
from .forms import ScentForm, WaftingForm


# views-----------

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def scents_index(request):
    scents = Scent.objects.filter(user=request.user)
    return render(request, 'scents/index.html', {'scents': scents})


@login_required
def scents_detail(request, scent_id):
    scent = Scent.objects.get(id=scent_id)
    powers_scent_doesnt_have = Power.objects.exclude(
        id__in=scent.powers.all().values_list('id'))
    wafting_form = WaftingForm()

    context = {
        'scent': scent,
        'wafting_form': wafting_form,
        'powers': powers_scent_doesnt_have
    }
    return render(request, 'scents/detail.html', context)


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


@login_required
def assoc_power(request, scent_id, power_id):
    Scent.objects.get(id=scent_id).powers.add(power_id)
    return redirect('detail', scent_id=scent_id)


@login_required
def new_scent(request):
  # if a post request is made to this view function
    if request.method == 'POST':
        # save the form data to a variable
        form = ScentForm(request.POST)
        if form.is_valid():
            # if the form passes validation, create a new instance
            # of the cat model through the ModelForm (CatForm)
            scent = form.save(commit=False)
            scent.user = request.user
            scent.save()
            # redirect the user to the new cat's detail page
            return redirect('detail', scent.id)
    else:
        # if a get request is made to this view function,
        # create new, empty instance of the CatForm
        form = ScentForm()
    # create a context dictionary
    context = {'form': form}
    # pass the form (through context) to the cat_form template
    return render(request, 'scents/scent_form.html', context)


# @login_required
# def scents_update
# @login_required
# def scents_delete

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class PowerList(LoginRequiredMixin, ListView):
    model = Power


class PowerDetail(LoginRequiredMixin, DetailView):
    model = Power


class PowerCreate(LoginRequiredMixin, CreateView):
    model = Power
    fields = '__all__'


class PowerUpdate(LoginRequiredMixin, UpdateView):
    model = Power
    fields = ['name', 'description']


class PowerDelete(LoginRequiredMixin, DeleteView):
    model = Power
    success_url = '/powers/'
