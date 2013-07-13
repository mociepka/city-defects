from django.contrib import admin
from .models import Defect, Image, Tag


class ImageInline(admin.TabularInline):

    model = Image


class DefectAdmin(admin.ModelAdmin):

    inlines = [ImageInline]


admin.site.register(Defect, DefectAdmin)
admin.site.register(Image)
admin.site.register(Tag)
