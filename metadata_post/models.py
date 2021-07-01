"""Models to links tables between post and their data"""
#Django
from django.db import models

#Local
from posts.models import Posts, Languages, Images, Tags


# Create your models here.
class PostsLanguages(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    language_id = models.ForeignKey(Languages, models.DO_NOTHING)

    def __str__(self):
        return f'The post {self.post_id.title} is in {self.language_id.language}'

    class Meta:
        managed = False
        db_table = 'posts_languages'


class PostsTags(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    tag_id = models.ForeignKey(Tags, models.DO_NOTHING)

    def __str__(self):
        return f'The post {self.post_id.title} have the {self.tag_id.tag_name} tag'
    class Meta:
        managed = False
        db_table = 'posts_tags'


class PostImages(models.Model):
    post_id = models.ForeignKey(Posts, models.DO_NOTHING)
    image_id = models.ForeignKey(Images, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'post_images'

    def __str__(self):
        return f'This image correspond to {self.post_id.title} post'