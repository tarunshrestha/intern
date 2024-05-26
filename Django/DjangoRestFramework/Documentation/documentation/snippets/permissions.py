from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read can be done by anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #  write is only for owner.
        return obj.owner == request.user