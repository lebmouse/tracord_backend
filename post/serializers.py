from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
  # pk = serializers.IntegerField(read_only=True)
  create_at = serializers.DateTimeField()
  singer = serializers.CharField(max_length=50)
  title = serializers.CharField(max_length=100)
  content = serializers.CharField(max_length=600)
  temperature = serializers.IntegerField()
  location = serializers.CharField(max_length=150)
  cover_img = serializers.ImageField()
