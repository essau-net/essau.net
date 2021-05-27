from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(unique=True, max_length=30)
    username = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=255)
    permission_level = models.CharField(max_length=9, blank=True, null=True)
    url_perfil_image = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    active = models.IntegerField(blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'users'