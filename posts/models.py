"""Models to post data and its components"""
#Djangos apps
from django.db import models

#Local apps

from users.models import User


class Categories(models.Model):
    category_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.category_name


class Posts(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    category_id = models.ForeignKey(Categories, models.DO_NOTHING)
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=9, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title} by @{self.user_id.username}'

    class Meta:
        managed = False
        db_table = 'posts'


class Images(models.Model):
    url_image = models.CharField(max_length=255, blank=True, null=True)
    image_format = models.CharField(max_length=3, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'images'

    def __str__(self):
        return f'The image have the path {self.url_image} and its format is {self.image_format}'


class Comments(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'

    def __str__(self):
        return f'Commnet created by @{self.user_id.username} in the {self.post_id.title} post'


class Languages(models.Model):
    language = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'languages'

    def __str__(self):
        return self.language


class Tags(models.Model):
    tag_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tags'

    def __str__(self):
        return self.tag_name