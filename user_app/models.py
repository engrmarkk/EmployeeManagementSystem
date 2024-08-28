from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def hexid():
    # Generate a UUID4 (randomly generated UUID)
    unique_id = uuid.uuid4()
    # Convert the UUID to a hex string without dashes
    hex_id = unique_id.hex
    return hex_id


class Positions(models.Model):
    id = models.CharField(primary_key=True, default=hexid, editable=False, unique=True, max_length=50)
    name = models.CharField(max_length=255)


# Create your models here.
class OrganizationUsers(AbstractUser):
    id = models.CharField(primary_key=True, default=hexid, editable=False, unique=True, max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    left = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password", "position"]

    def __str__(self):
        return self.email


class EmployeeProfile(models.Model):
    id = models.CharField(primary_key=True, default=hexid, editable=False, unique=True, max_length=50)
    user = models.ForeignKey(OrganizationUsers, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    hired_date = models.DateField()

    def __str__(self):
        return self.user


class LeaveRequests(models.Model):
    id = models.CharField(primary_key=True, default=hexid, editable=False, unique=True, max_length=50)
    user = models.ForeignKey(OrganizationUsers, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Pending",
                              choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")])
    admin_comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user
