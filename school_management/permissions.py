from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Only staff users can add, update, or delete data.
    Other users have read-only access
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
