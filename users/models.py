from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.timezone import now

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles(models.TextChoices):
    USER = "user"
    ADMIN = "admin"


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    phone = PhoneNumberField(null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=[UserRoles])
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]
    objects = UserManager()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


    class Meta:
        ordering = ['-last_login']
