from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=255)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()
    updated_at = models.DateTimeField()
    url_img_profile = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'users'

