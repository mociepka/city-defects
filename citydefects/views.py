from django.template.response import TemplateResponse
from django.conf import settings


def home(request):
    return TemplateResponse(request, 'home.html', {
        'map': {'lat': settings.DEFAULT_LAT, 'lng': settings.DEFAULT_LNG,
                'zoom': 15}
    })
