from django import forms
from .models import Scent, Wafting


class ScentForm(forms.ModelForm):

    class Meta:
        model = Scent
        fields = ("name", "location", "characteristics", "rating")


class WaftingForm(forms.ModelForm):
    class Meta:
        model = Wafting
        fields = ['date', 'emotion']
