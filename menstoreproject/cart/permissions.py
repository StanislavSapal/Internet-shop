from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.owner == request.user
        else:
            return obj.owner == request.cart.token
