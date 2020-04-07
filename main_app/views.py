from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Define the home view


def home(request):
    return HttpResponse('<h1>Scent Collector (✿ヘᴥヘ)</h1>')


def about(request):
    return render(request, 'about.html')


def scents_index(request):
    return render(request, 'scents/index.html', {'scents': scents})


class Scent:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, location, characteristics, rating):
        self.name = name
        self.location = location
        self.characteristics = characteristics
        self.rating = rating


scents = [
    Scent('Tree', 'In front of home', 'Woodsy, bark, touch of pee', 6),
    Scent('Pole', '23rd & Florida', 'Metalic, urine, frequently visited', 2),
    Scent('Marc', 'Valencia & 19th', 'Sweet, savory, with notes of mountain', 10)
]
