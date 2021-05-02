from django.conf import settings
from django.db import models
from django.utils.text import slugify

from appsutils.models import BaseEntity


User = settings.AUTH_USER_MODEL


class Group(BaseEntity):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]


class GroupMember(BaseEntity):
    group = models.ForeignKey(Group, related_name="memberships", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_in_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
