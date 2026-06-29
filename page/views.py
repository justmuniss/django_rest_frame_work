from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.
class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogListAPIView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
     