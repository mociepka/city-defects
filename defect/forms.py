from django import forms
from .models import Defect


class DefectForm(forms.ModelForm):

    class Meta:
        model = Defect
        fields = ['street', 'title', 'description', 'tags', 'lat', 'lng']
        widgets = {
             'lat': forms.HiddenInput,
             'lng': forms.HiddenInput,
        }
