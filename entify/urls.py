from django.urls import path, include, re_path

from entify.dashboard.views import NodeListView, NodeView, CreateNodeView


urlpatterns = [
    path('api/', include('entify.api.urls')),
    path('dashboard/', include('entify.dashboard.urls')),
]
