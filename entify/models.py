from django.db import models
import uuid
from base62 import encode as b62encode


class IdentifierType(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id) or '-'


class Image(models.Model):
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='images')
    url = models.URLField()
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('url',)

    def __str__(self):
        return self.url


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
            self.identifier = b62encode(int(self.id))
        if not self.uri:
            self.uri = f'spacify:{self.type}:{self.identifier}'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class ExternalIdentifier(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='external_identifiers')
    type = models.ForeignKey(IdentifierType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('type', 'value')
        ordering = ('type', 'value')

    def __str__(self):
        return f'{self.type}:{self.value}'


class Type(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id) or '-'
