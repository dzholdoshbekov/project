from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer