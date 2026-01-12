from django.contrib import admin

from .models import Node, Type


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'identifier',
        'uri'
    )

    search_fields = ['name', 'type', 'slug']

    list_filter = ['type']


@admin.register(Type)
class NodeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    search_fields = ['id', 'name']

