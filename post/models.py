from django.db import models
from PIL import Image
import os
import datetime
# Create your models here.


def wrapper(instance, filename):
    path = 'images/'
    now = instance.create_at.strftime('%Y%m%d')
    filename = now + '.jpg'
    return os.path.join(path, filename)

class Post(models.Model):
    singer = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    temperature = models.IntegerField()
    location = models.CharField(max_length=150)
    cover_img = models.ImageField(blank=True, upload_to=wrapper)
    create_at = models.DateTimeField('create date', blank=False)

    def __str__(self):
        return str(self.create_at)

    class Meta:
        ordering = ['create_at']
