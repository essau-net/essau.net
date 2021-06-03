from django.db import models


# Create your models here.
class Images(models.Model):
    url_image = models.CharField(max_length=255, blank=True, null=True)
    image_format = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'

        
class TagsImg(models.Model):
    tags_img = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags_img'


class Tagsimg_Images(models.Model):
    tagimg_id = models.ForeignKey(TagsImg, models.DO_NOTHING)
    image_id = models.ForeignKey(Images, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tagsimg_images'