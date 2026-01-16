from django.urls import path, include, re_path

from entify.views import NodeListView, NodeView, CreateNodeView


urlpatterns = [
    path('api/', include('entify.api.urls')),
    path('nodes', NodeListView.as_view(), name='nodes'),
    re_path(r'node/create$', CreateNodeView.as_view(), name='create_node'),
    re_path(r'node/(?P<node_id>([a-zA-Z0-9\-]+))/overview', NodeView.as_view(), name='node_overview'),
]
