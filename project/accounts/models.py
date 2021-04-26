import enum

from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models


# Create your domain models here.

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
        'CustomUser',
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
        'CustomUser',
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


class AccountManager(BaseUserManager):
    """ Extend BaseUserManager to cater for the custom user model.

    Define 3 methods: create_user(), create_superuser(), validate_user_details()

    Ref: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
    Ref: for link specific to the manager for a custom user model:
    https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model

    AbstractBaseUser and BaseUserManager are importable from django.contrib.auth.base_user so that
    they can be imported without including django.contrib.auth in INSTALLED_APPS.

    The importance of this class is as follows:
    You define a custom manager for your user model.
    If your user model defines username, email, is_staff, is_active, is_superuser, last_login, and date_joined fields
    the same as Django’s default user, you can install Django’s UserManager;
    however, if your user model defines different fields, you’ll need to define a custom manager
    that extends BaseUserManager providing two additional methods:

    BaseUserManager provides the following utility methods:

    class models.BaseUserManager
        class method normalize_email(email)
            Normalizes email addresses by lowercasing the domain portion of the email address.

        get_by_natural_key(username)
            Retrieves a user instance using the contents of the field nominated by USERNAME_FIELD.

        make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            Returns a random password with the given length and given string of allowed characters.
            Note that the default value of allowed_chars doesn’t contain letters that can cause user confusion,
            including:
                i, l, I, and 1 (lowercase letter i, lowercase letter L, uppercase letter i, and the number one)
                o, O, and 0 (lowercase letter o, uppercase letter o, and zero)
    """

    def create_user(self, first_name: str, email: str, username: str, phone_number: str, password: str = None):
        """ Create superuser based on the custom user model.

        The prototype of create_user() should accept the username field, plus all required fields as arguments.
        For example, if your user model uses email as the username field, and has date_of_birth as a required field,
        then create_user should be defined as:

        def create_user(self, email, date_of_birth, password=None):
            # create user here
            ...

        :param first_name:
        :param email:
        :param username:
        :param phone_number:
        :param password:
        :return:
        """
        self.validate_user_details(email, first_name, username, phone_number)
        user = self.model(
            first_name=first_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name: str, email: str, username: str, phone_number: str, password: str = None):
        """ Create superuser based on the custom user model.

        The prototype of create_superuser() should accept the username field, plus all required fields as arguments.
        For example, if your user model uses email as the username field, and has date_of_birth as a required field,
        then create_superuser should be defined as:

        def create_superuser(self, email, date_of_birth, password=None):
            # create superuser here
            ...

        :param first_name:
        :param email:
        :param username:
        :param phone_number:
        :param password:
        :return:
        """
        self.validate_user_details(email, first_name, username, phone_number)
        user = self.create_user(
            first_name=first_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    @staticmethod
    def validate_user_details(email: str, first_name: str, username: str, phone_number: str):
        """ Validate all required user details.

        :param email:
        :param first_name:
        :param username:
        :param phone_number:
        :return: noting
        :raises ValueError: when anyone of first_name, username, email, phone_number is missing
        """
        if not first_name:
            raise ValueError("User must have a first name")
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        if not phone_number:
            raise ValueError("User must have a phone number")


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseEntity):
    """ Overrides the default Django user model.

    Attributes:
        Django mandatory attributes:
            email, username, date_joined, last_login, is_active, is_admin, is_superuser, is_staff
        Non-mandatory attributes:
            first_name, last_name, gender, phone_number
    """
    # Start of mandatory attributes required when overriding the default django model
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    date_joined = models.DateField(null=True, blank=True, auto_now_add=True)
    last_login = models.DateField(null=True, blank=True, auto_now=True)
    is_active = models.BooleanField(default=True)  # Set to True so that every user is active by default
    is_admin = models.BooleanField(default=False)  # Set to False so that every user is not an admin
    is_superuser = models.BooleanField(default=False)  # Set to False so that every user is not a staff
    is_staff = models.BooleanField(default=False)
    # End of mandatory attributes

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        null=True, blank=True,
        max_length=255,
        default=None,
        choices=[(record.name, record.value) for record in Gender]
    )
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone_number', 'email']  # List of all required fields including the username
    objects = AccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Default to True so that every yser has access to this module.

        :param app_label:
        :return:
        """
        return True

    class Meta:
        db_table = 'users'
        ordering = ('first_name', 'last_name', 'username', 'email')
        default_permissions = ()
        permissions = (
            ('custom_view_security_menu', 'View Security Menu'),
            ('custom_add_user', 'Add User'),
            ('custom_edit_user', 'Edit User'),
            ('custom_view_users', 'View Users'),
            ('custom_add_role', 'Add Role'),
            ('custom_edit_role', 'Edit Role'),
            ('custom_view_roles', 'View Roles'),
        )