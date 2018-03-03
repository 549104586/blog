from django.db import models

# Create your models here.
class Article(models.Model):

        title = models.CharField(max_length=100)
        content = models.CharField(max_length=200)
        comment = models.CharField(max_length=200)
