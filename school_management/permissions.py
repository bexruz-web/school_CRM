from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Only staff users can add, update, or delete data.
    Other users have read-only access
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Permission is granted if the user has role='teacher'.
    Other users can only read (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', None) == 'teacher'
