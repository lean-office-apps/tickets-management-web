from django.db import models
from django.urls import reverse
from django.utils import timezone

from tickets.models import Ticket
from appsutils.models import BaseEntity

# TODO: create 'comment' model, views and all


# Create your models here.

class Comment(BaseEntity):
    post = models.ForeignKey(
        'Ticket',       # TODO: should be updated so that a comment could be added to other models as well
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
