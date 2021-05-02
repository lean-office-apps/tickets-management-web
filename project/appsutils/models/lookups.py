import enum

from .base_entity import BaseEntity
from django.db import models


class LookUpCategories(enum.Enum):
    GENDER = "Gender"  # Represents a person's gender

    def __str__(self):
        return self.name


class LookUp(BaseEntity):
    """
    Represents lookups in the ticket management system. Lookups can be selectable values displayed in dropdowns
    """
    name = models.CharField(null=False, max_length=255)
    category = models.CharField(null=True, blank=True,
                                max_length=255, default=None,
                                choices=[(record.name, record.value) for record in LookUpCategories],
                                verbose_name='LookUp')

    def __eq__(self, other):
        return (other and isinstance(other, LookUp)) and (self.id == other.id if self.id else other == self)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'log_lookups'
        ordering = ('created_on', 'name')
        default_permissions = ()
        permissions = (('custom_add_lookup', 'Add LookUp'), ('custom_edit_lookup', 'Edit LookUp'),
                       ('custom_view_lookups', 'View LookUps'))

