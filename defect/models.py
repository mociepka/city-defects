import re

from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode
from easy_thumbnails.fields import ThumbnailerImageField


User = settings.AUTH_USER_MODEL


class Tag(models.Model):

    value = models.CharField(max_length=50, primary_key=True)
    hits = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        self.value = self.value.replace(' ', '-').strip().lower()
        return super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'#%s' % self.value.replace('-', ' ')


class Defect(models.Model):

    title = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    street = models.CharField(max_length=255)
    lat = models.FloatField(_('Latitude'), default=settings.DEFAULT_LAT)
    lng = models.FloatField(_('Longitude'), default=settings.DEFAULT_LNG)
    publicated = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             related_name='reported_defects')
    tags = models.ManyToManyField(Tag)
    hits = models.IntegerField(default=0, editable=False)

    def get_slug(self):
        slug = unidecode(self.title)
        slug = re.sub(r'[^\w\s-]', '', slug).strip().lower()
        return mark_safe(re.sub(r'[-\s]+', '-', slug))

    def __unicode__(self):
        return self.title


class Image(models.Model):

    defect = models.ForeignKey(Defect, related_name='images')
    image = ThumbnailerImageField(upload_to='defects')
    title = models.CharField(max_length=80, default='', blank=True)
