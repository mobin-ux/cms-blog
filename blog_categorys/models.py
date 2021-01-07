from django.db import models

class Categorys(models.Model):
    title = models.CharField(blank=True, null=True, max_length=999)
    slug = models.SlugField(blank=True, null=True, max_length=999)
    ReleaseStatus  = models.BooleanField(blank=True,null=True,default=False)

    def __str__(self):
        return self.title



class Categorys_Article(models.Model):
    Article_id = models.IntegerField(blank=True, null=True)
    Category_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.Article_id}'




