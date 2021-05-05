from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from api.managers import CustomUserManager
from api.models.role import Role


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    bio = models.TextField(
        verbose_name='О себе',
        max_length=512,
        null=True,
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )

    objects = CustomUserManager()

    @property
    def is_admin(self):
        return (self.role == Role.ADMIN
                or self.is_superuser
                or self.is_staff)

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR


User = get_user_model()
