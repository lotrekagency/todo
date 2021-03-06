from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Media(models.Model):
    file = models.FileField(upload_to='uploads/')
    alt = models.CharField(max_length=200, null=True, blank=True)
    description  = models.TextField( null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.file.url

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    attachments = models.ForeignKey(Media, null=True, blank=True)
    users = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title
