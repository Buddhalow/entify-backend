from django.forms import ModelForm

from .models import Node


class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields = [
            'name',
            'type',
            'identifier',
            'external_ids'
        ]
