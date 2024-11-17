from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

