from rest_framework import permissions, request


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.author == request.user

class IsOwner(permissions.BasePermission):

    # def has_permission(self, request, view):
    #     print('has_permission: request.user=', request.user)
    #     return True
    def has_object_permission(self, request, view, obj):
        print('has_object_permission: obj.author=', obj.author, 'request.user=', request.user)
        return obj.author == request.user