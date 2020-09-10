from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import TMUserManager

from genre.models import Genre

from decimal import Decimal

class TMUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique=True, primary_key=True)
    nickname = models.CharField(max_length = 50, unique=True)
    name = models.CharField(max_length = 30, default="username")
    date_of_birth = models.DateField(default = timezone.now)
    phone_number = models.CharField(max_length = 11, default="010-1234-5678")
    address = models.CharField(max_length = 200, null=True, blank=True)
    is_author = models.BooleanField(default=False)  #작가 등록 여부
    prefer_genre = models.ManyToManyField(Genre, related_name='prefer_users') #선호 장르

    point = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TMUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

class TMAuthor(models.Model):
    author_name = models.CharField(max_length = 50, unique=True)
    introduce = models.CharField(max_length = 500, null=True, blank=True)
    page_link = models.CharField(max_length = 300, null=True, blank=True)
    sns_link = models.CharField(max_length = 300, null=True, blank=True)
    portfolio = models.FileField(upload_to='portfolios',null=True, blank=True)
    opening_date = models.DateField(default = timezone.now)
    follower_num = models.PositiveIntegerField(default=0)
    tomag_num = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(
        TMUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.author_name