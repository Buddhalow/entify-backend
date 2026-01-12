from django.db import models
import uuid
from base62 import encode as b62encode


class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identifier = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255)
    attributes = models.JSONField(default=dict, blank=True)
    uri = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    external_ids = models.JSONField(default=dict, blank=True)
    external_urls = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = b62encode(self.id.int)
        if not self.uri:
            self.uri = f'spacify:{self.type}:{self.identifier}'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Type(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.id or '-'
