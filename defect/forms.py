from django import forms

from .models import Defect, Image


class DefectForm(forms.ModelForm):

    class Meta:
        model = Defect
        fields = ['street', 'title', 'description', 'tags', 'lat', 'lng']
        widgets = {
             'lat': forms.HiddenInput,
             'lng': forms.HiddenInput,
        }


class DefectImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']
