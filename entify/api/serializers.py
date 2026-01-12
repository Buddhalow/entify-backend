from rest_framework import serializers

from entify.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            'id',
            'identifier',
            'name',
            'description',
            'external_ids',
            'external_urls',
            'type',
            'uri',
            'created',
            'updated',
            'deleted',
        ]

    uri = serializers.SerializerMethodField()

    def get_uri(self, obj):
        return f"spacify:{obj.type}:{obj.identifier}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.attributes)

        return data
