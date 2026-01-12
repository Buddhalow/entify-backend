from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from entify.models import Node
from .serializers import NodeSerializer


class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeAPIView(APIView):
    def get(self, request, type=None, slug=None):
        nodes = Node.objects.filter(type=type, slug=slug).first()
        serializer = NodeSerializer(nodes, many=True)
        return Response(serializer.data)
