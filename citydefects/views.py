from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import simplejson
from django.views.decorators.cache import cache_page
from django.forms.models import model_to_dict
from easy_thumbnails.files import get_thumbnailer
import requests

from defect.forms import DefectForm
from defect.models import Defect

DAY = 86400


def get_image_obj(image):
    return {
        'small': get_thumbnailer(image.image)['small'].url,
        'big': get_thumbnailer(image.image)['big'].url
    }


def home(request):
    form = DefectForm(request.POST or None)
    defects_qs = Defect.objects.select_related('images').filter(publicated=False)
    defects = []
    for defect_obj in defects_qs:
        defect = model_to_dict(defect_obj)
        defect['images'] = [get_image_obj(image)
                            for image in defect_obj.images.all()]
        defects.append(defect)
    if form.is_valid():
        form.save()
        return redirect('home')
    return TemplateResponse(request, 'home.html', {
        'map': {'lat': settings.DEFAULT_LAT,
                'lng': settings.DEFAULT_LNG,
                'zoom': 15},
        'form': form,
        'defects': defects
    })


def get_street(result):
    labels = [component['long_name'] for component in
             result['address_components'] if
             component['types'][0] in ['street_number', 'route']]
    labels.reverse()
    return {'label': ' '.join(labels),
            'lat': result['geometry']['location']['lat'],
            'lng': result['geometry']['location']['lng'],
            'bounds': result['geometry']['bounds']}


# https://developers.google.com/maps/terms
# paragraph 10.1.3 b
@cache_page(DAY * 30)
def street_cache(request):
    url = settings.GOOGLE_GEOCODE_URL % {'address': request.GET.get('address')}
    response = requests.get(url)
    json = response.json()
    if json['status'] == 'OK':
        addresses = [get_street(result) for result in json['results']
                   if u'route' in result['types'] or
                   u'street_address' in result['types']]
        return HttpResponse(simplejson.dumps(addresses))
    return HttpResponse('[]')
