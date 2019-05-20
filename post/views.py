from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_seriacreate_atlizer = PostSerializer(posts, many=True)
        return JSONResponse(posts_seriacreate_atlizer.data)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JSONResponse(post_serializer.data, status=status.status.HTTP_202_CREATED)
        return JSONResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def post_year(request, year):
    if request.method == 'GET':
        posts = Post.objects.filter(create_at__year=year)
        posts_serializer = PostSerializer(posts, many=True)
        return JSONResponse(posts_serializer.data)


@csrf_exempt
def post_month(request, year, month):
    if request.method == 'GET':
        posts = Post.objects.filter(
            create_at__year=year).filter(create_at__month=month)
        posts_serializer = PostSerializer(posts, many=True)
        return JSONResponse(posts_serializer.data)


@csrf_exempt
def post_date(request, year, month, date):
    if request.method == 'GET':
        posts = Post.objects.filter(create_at__year=year).filter(
            create_at__month=month).filter(create_at__day=date)
        posts_serializer = PostSerializer(posts, many=True)
        return JSONResponse(posts_serializer.data)


# Create your views here.
