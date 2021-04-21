from django.conf import settings
from django.db import models

# Create your models here.
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class Group(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through="GroupMember")

    # TODO: add AUTH_USER_MODEL to settings.py

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_in_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
