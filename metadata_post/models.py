"""Models to links tables between post and their data"""
#Django
from django.db import models

#Local
from posts.models import Posts, Languages, Images, Tags


# Create your models here.
class PostsTags(models.Model):
    post = models.ForeignKey(Posts, models.DO_NOTHING)
    tag = models.ForeignKey(Tags, models.DO_NOTHING)

    def __str__(self):
        return f'The post {self.post.title} have the {self.tag.tag_name} tag'
    class Meta:
        managed = False
        db_table = 'posts_tags'


class PostImages(models.Model):
    post = models.ForeignKey(Posts, models.DO_NOTHING)
    image = models.ForeignKey(Images, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'post_images'

    def __str__(self):
        return f'This image correspond to {self.post.title} post'