###created
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission): ###Base permission class that Django rest framework provides for making your own custom permissions
    """"Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: ###safe methods such as GET
            return True

        return obj.id == request.user.id
