from rest_framework_extensions.routers import ExtendedDefaultRouter

from .viewsets import NodeViewSet

router = ExtendedDefaultRouter()

router.register('nodes', NodeViewSet)
