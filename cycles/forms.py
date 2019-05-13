from django import forms
from .models import Cycle, Location, Pickcycle, Dropcycle


class NewCycleForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = ('name', 'model', 'image', 'rent')


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('area', 'near_by', 'near_by_t', 'gps_lat', 'gps_lon')


class PickForm(forms.ModelForm):

    class Meta:
        model = Pickcycle
        fields = ('cycle_id', 'picked_by')
        widgets = {
            'cycle_id': forms.HiddenInput(),
            'picked_by': forms.HiddenInput()
        }


class DropForm(forms.ModelForm):

    class Meta:
        model = Dropcycle
        fields = ('pick_id',)
        widgets = {
            'pick_id': forms.HiddenInput()
        }
