from django.urls import re_path, path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .viewsets import NodeAPIView
from .routers import router


urlpatterns = [
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    re_path(r'^(?P<type>\w+)/(?P<slug>\w+)$', NodeAPIView.as_view(), name='node'),
    *router.urls
]
