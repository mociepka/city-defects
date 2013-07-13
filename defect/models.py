from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Defect(models.Model):

    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    description = models.TextField()
    street = models.CharField(max_length=255)
    lat = models.FloatField('Latitude', default=settings.DEFAULT_LAT)
    lng = models.FloatField('Longitude', default=settings.DEFAULT_LNG)
    publicated = models.BooleanField()
    user = models.ForeignKey(User)
