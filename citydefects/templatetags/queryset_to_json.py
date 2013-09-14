from decimal import Decimal
from django import template
from django.db import models
from django.forms.models import model_to_dict
from django.utils import simplejson
from django.utils.html import mark_safe

register = template.Library()


class DjangoJSONEncoder(simplejson.JSONEncoder):

    def __init__(self, *args, **kwargs):
        self.keys = kwargs.pop('keys', None)

        super(DjangoJSONEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, models.query.QuerySet):
            return list(obj)

        if isinstance(obj, models.Model):
            model_dict = model_to_dict(obj, fields=self.keys)
            if not self.keys or 'pk' in self.keys or 'id' in self.keys:
                model_dict['id'] = obj.pk
            return model_dict

        if issubclass(type(obj), models.fields.files.FieldFile):
            return obj.url

        if isinstance(obj, Decimal):
            return float(obj)

        return super(DjangoJSONEncoder, self).default(str(obj))


@register.filter
def json(var, keys=None):
    if keys:
        keys = keys.split(',')

    return mark_safe(simplejson.dumps(var, cls=DjangoJSONEncoder, keys=keys))
