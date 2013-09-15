from rest_framework import routers
from rest_framework.viewsets import mixins, GenericViewSet

from models import Defect


class DefectsViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, GenericViewSet):

    model = Defect

    def pre_save(self, obj):
        obj.user = self.request.user
        super(DefectsViewSet, self).pre_save(obj)

router = routers.DefaultRouter()
router.register(r'defects', DefectsViewSet)
