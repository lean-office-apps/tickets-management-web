# tickets/models.py

from django.db import models
from django.urls import reverse

import misaka

from groups.models import Group


# Create your models here.
class Ticket(models.Model):
    summary = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='new')
    description = models.TextField()
    description_html = models.TextField(editable=False)     # For html rendering of the description
    group = models.ForeignKey(Group, related_name="tickets", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary

    def save(self, *args, **kwargs):
        self.description_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']


# TODO: create 'comment' model, views and all