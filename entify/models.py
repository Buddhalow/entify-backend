from django.db import models
import uuid
from base62 import encode as b62encode


class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    attributes = models.JSONField(default=dict)
    uri = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    external_ids = models.JSONField(default=dict)
    external_urls = models.JSONField(default=dict)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = b62encode(self.id.bytes)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
