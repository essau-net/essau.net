"""Models to post data and its components"""
#Djangos apps
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

#Local apps

from users.models import User


class Categories(models.Model):
    category = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.category


class Posts(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    title = models.CharField(max_length=150)
    url_markdown_file = models.CharField(max_length=500, blank=False, null=False)
    url_html_file = models.CharField(max_length=500, blank=False, null=False)
    published = models.IntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    publicated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'

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
    user = models.ForeignKey(User, models.DO_NOTHING)
    post = models.ForeignKey(Posts, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        managed = False
        db_table = 'comments'

    def __str__(self):
        return f'Commnet created by @{self.user.username} in the {self.post.title} post'


class Languages(models.Model):
    language = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'languages'

    def __str__(self):
        return self.language


class Tags(models.Model):
    tag = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tags'

    def __str__(self):
        return self.tag