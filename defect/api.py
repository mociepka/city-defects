from rest_framework import routers
from rest_framework.viewsets import mixins, GenericViewSet

from models import Defect


class DefectsViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, GenericViewSet):

    model = Defect

router = routers.DefaultRouter()
router.register(r'defects', DefectsViewSet)
