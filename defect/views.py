from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.views.decorators.http import require_POST

from defect.forms import DefectImageForm
from defect.models import Defect, Image


#@require_POST
def addimage(request, defect_id):
    try:
        defect = Defect.objects.get(id=defect_id)
    except Defect.DoesNotExist:
        return HttpResponseNotFound('Not found')
    image = Image(defect=defect)
    form = DefectImageForm(files=request.FILES or None, instance=image)
    if form.is_valid():
        form.save()
        return HttpResponse(image.image.url)
    return HttpResponseBadRequest('Bad image')
