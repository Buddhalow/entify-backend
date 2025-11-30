from django.urls import re_path

from .views import NodeAPIView

from .router import router

urlpatterns = [
    re_path(r'^(?P<type>\w+)/(?P<slug>\w+)$', NodeAPIView.as_view(), name='node'),
    *router.urls
]
