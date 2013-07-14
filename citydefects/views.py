from defect.forms import DefectForm
from django.conf import settings
from django.shortcuts import redirect
from django.template.response import TemplateResponse


def home(request):
    form = DefectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return TemplateResponse(request, 'home.html', {
        'map': {'lat': settings.DEFAULT_LAT, 'lng': settings.DEFAULT_LNG,
                'zoom': 15},
        'form': form
    })
