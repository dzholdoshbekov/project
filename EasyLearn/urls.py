from django.urls import path, include
from rest_framework import routers
from .views import *
from .views import UserList, UserDetail

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]