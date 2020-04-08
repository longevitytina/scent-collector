from django.forms import ModelForm
from .models import Wafting


class WaftingForm(ModelForm):
    class Meta:
        model = Wafting
        fields = ['date', 'emotion']
