from django.conf import settings


def facebook(request):
    return {'FB_API_ID': getattr(settings, 'FB_API_ID', '')}
