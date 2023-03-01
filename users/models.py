from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="user_details"
    )
    age = models.PositiveSmallIntegerField(default=0)
    dob = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    favourite_team = models.CharField(max_length=100, null=True, blank=True)
    favourite_player = models.CharField(max_length=100, null=True, blank=True)
    balance = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    rarity = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email


class Avatar(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="avatar"
    )
    bgColor = models.CharField(max_length=100, null=True, blank=True)
    earSize = models.CharField(max_length=100, null=True, blank=True)
    eyeBrowStyle = models.CharField(max_length=100, null=True, blank=True)
    eyeStyle = models.CharField(max_length=100, null=True, blank=True)
    faceColor = models.CharField(max_length=100, null=True, blank=True)
    glassesStyle = models.CharField(max_length=100, null=True, blank=True)
    hairColor = models.CharField(max_length=100, null=True, blank=True)
    hairStyle = models.CharField(max_length=100, null=True, blank=True)
    hatColor = models.CharField(max_length=100, null=True, blank=True)
    hatStyle = models.CharField(max_length=100, null=True, blank=True)
    mouthStyle = models.CharField(max_length=100, null=True, blank=True)
    noseStyle = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=100, null=True, blank=True)
    shirtColor = models.CharField(max_length=100, null=True, blank=True)
    shirtStyle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sex
