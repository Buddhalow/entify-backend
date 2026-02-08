import json

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from entify.models import Node
from .serializers import NodeSerializer


class NodeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated | HasAPIKey]
    queryset = Node.objects.all()
    serializer_class = NodeSerializer



class UpsertNodeAPIView(APIView):
    permission_classes = [IsAuthenticated | HasAPIKey]

    def get(self, request, type=None, slug=None):
        body = json.loads(request.body)
        node_type = body.get('type')
        name = body.get('name')
        slug = body.get('slug', None)
        id = body.get('id')
        
        node, created = Node.objects.update_or_create(
            id=id,
            type=node_type,
            name=name,
            slug=slug
        )
        return Response(
            instance=node
        ).data


class NodeAPIView(APIView):
    permission_classes = [IsAuthenticated | HasAPIKey]
    def get(self, request, type=None, slug=None):
        nodes = Node.objects.filter(type=type, slug=slug).first()
        serializer = NodeSerializer(nodes, many=True)
        return Response(serializer.data)
