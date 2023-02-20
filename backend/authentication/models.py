from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)

    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('superuser status', default=False)
    is_active = models.BooleanField('active status', default=True)
    last_login = models.DateTimeField(
        'last login', null=True, default=None)
    pass
