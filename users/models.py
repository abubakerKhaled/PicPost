from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profiles/%Y/%m/%d/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def avatar(self):
        try:
            avatar = self.profile_picture.url
        except:
            avatar = static("images/avatar_default.svg")
        return avatar
    def __str__(self):
        return f'Profile of {self.user.username}'
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

