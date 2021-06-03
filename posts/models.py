#Djangos apps
from django.db import models

#Local apps
from images.models import Images
from users.models import User



class Categories(models.Model):
    category_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'categories'


class Posts(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    category_id = models.ForeignKey(Categories, models.DO_NOTHING)
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=9, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts'


class Comments(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class Languages(models.Model):
    language = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'languages'


class PostImages(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    image_id = models.ForeignKey(Images, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_images'


class PostsLanguages(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    language_id = models.ForeignKey(Languages, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_languages'


class Tags(models.Model):
    tag_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tags'


class PostsTags(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    tag_id = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'posts_tags'