# tickets/models.py

from django.db import models
from django.urls import reverse


# Create your models here.
class Ticket(models.Model):
    summary = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='new')
    description = models.TextField()

    def __str__(self):
        return self.summary

    class Meta:
        ordering = ['-created_on']
