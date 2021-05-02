import enum

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL


class RecordStatus(enum.Enum):
    """
    This enum class represents the status of every record in the database.
    The status can be ACTIVE, DELETED, ACTIVE_LOCKED.
    The default record status for new database entries is ACTIVE.
    """
    ACTIVE = "Active"
    DELETED = "Delete"
    ACTIVE_LOCKED = "Active Locked"

    def __str__(self):
        return self.name


class Gender(enum.Enum):
    """
    This enum class represents the gender of users.
    Can be Male, Female, Other.
    """
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    def __str__(self):
        return self.name


class BaseEntity(models.Model):
    """
    This is the base class from which all database models inherit from.
    It contains audit trails of database entries:
    created_on
    created_by
    changed_on
    changed_by
    record_status
    """
    created_on = models.DateTimeField(
        default=timezone.now,
        null=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_by",
        related_query_name="%(app_label)s_%(class)ss_created_by",
    )
    changed_on = models.DateTimeField(
        default=timezone.now,
        null=True,
    )
    changed_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name="%(app_label)s_%(class)s_changed_by",
        related_query_name="%(app_label)s_%(class)ss_changed_by",
    )
    record_status = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        default=RecordStatus.ACTIVE.name,
        choices=[(record.name, record.value) for record in RecordStatus],
    )  # Record Status is a list of Tuple

    @property
    def __view_edit__(self):
        return 'View/Edit'

    class Meta:
        abstract = True  # Indicates that this is an abstract class inherited by other classes