from django.db import models
from blog_categorys.models import Categorys


class Articles(models.Model):
    title = models.CharField(blank=True,null=True,max_length=999)
    slug = models.SlugField(blank=True, null=True, max_length=999)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='Image_Of_Articles')
    CreationDate = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    ReleaseStatus = models.BooleanField(blank=True,null=True,default=False)

    def __str__(self):
        return self.title