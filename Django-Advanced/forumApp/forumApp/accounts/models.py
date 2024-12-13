from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         default=0,
#     )

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=100,
        unique=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )