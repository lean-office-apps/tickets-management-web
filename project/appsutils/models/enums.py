import enum

# Create your models here.


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
