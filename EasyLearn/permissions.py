from rest_framework import permissions, request
from rest_framework.generics import get_object_or_404

from EasyLearn.models import Course, User


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.author == request.user


class IsLessonBlockAuthor(permissions.BasePermission):
    """
    Custom permission to only allow lesson block authors to add, update, or delete the block.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, check if the user is the author of the course that the block belongs to
        course = Course.objects.all()
        return obj.course.author == request.user