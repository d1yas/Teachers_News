from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='news/')  
    description = models.TextField()
