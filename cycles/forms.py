from django import forms
from .models import Cycle, Location, Pickcycle, Dropcycle


class NewCycleForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = ('name', 'model', 'image', 'rent')
