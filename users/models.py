from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    url_profile_image = models.CharField(max_length=250, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'users'
