from django.db import models

# Create your models here.

class Post(models.Model):
  singer = models.CharField(max_length=50)
  title = models.CharField(max_length=100)
  content = models.TextField()
  temperature = models.IntegerField()
  location = models.CharField(max_length=150)
  cover_img = models.ImageField(blank=True, upload_to='%Y/%m/%d')
  create_at = models.DateTimeField('create date',blank=False)

  class Meta:
    ordering = ['create_at']


