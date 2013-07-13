from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


class Tag(models.Model):

    value = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)


class Defect(models.Model):

    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    street = models.CharField(max_length=255)
    lat = models.FloatField(_('Latitude'), default=settings.DEFAULT_LAT)
    lng = models.FloatField(_('Longitude'), default=settings.DEFAULT_LNG)
    publicated = models.BooleanField()
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)


class Image(models.Model):

    defect = models.ForeignKey(Defect, related_name='images')
    image = models.ImageField(upload_to='defects')
    title = models.CharField(max_length=80)
