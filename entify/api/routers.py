from rest_framework_extensions.routers import ExtendedDefaultRouter


router = ExtendedDefaultRouter()

router.register('nodes', NodeViewSet)