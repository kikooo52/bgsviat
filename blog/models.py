from django.db import models
from taggit.managers import TaggableManager

class MyBlog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __str__(self):
        return self.title