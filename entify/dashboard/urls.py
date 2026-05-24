from django.urls import path, include, re_path

from entify.dashboard.views import NodeListView, NodeView, CreateNodeView

from dashmin.urls import model_urlpatterns


urlpatterns = [
    path('node/', NodeListView.as_view(), name='nodes'),
    re_path(r'node/create$', CreateNodeView.as_view(), name='create_node'),
    re_path(r'node/(?P<node_id>([a-zA-Z0-9\-]+))/overview', NodeView.as_view(), name='node_overview'),
    path('node/', include(model_urlpatterns('entify', 'Node'))),
]
