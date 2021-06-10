from django.db import models


# Create your models here.
class Images(models.Model):
    url_image = models.CharField(max_length=255, blank=True, null=True)
    image_format = models.CharField(max_length=3, blank=True, null=True)
    
    def __str__(self):
        return f'The image have the path {self.url_image} and its format is {self.image_format}'

    class Meta:
        managed = False
        db_table = 'images'

        
class TagsImg(models.Model):
    tags_img = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.tags_img

    class Meta:
        managed = False
        db_table = 'tags_img'


class Tagsimg_Images(models.Model):
    tagimg_id = models.ForeignKey(TagsImg, models.DO_NOTHING)
    image_id = models.ForeignKey(Images, models.DO_NOTHING)

    def __str__(self):
        return f'The image {self.image_id.url_image} have the {self.tagimg_id.tags_img} tag'

    class Meta:
        managed = False
        db_table = 'tagsimg_images'