from django.db import models

class HomeFeed(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()