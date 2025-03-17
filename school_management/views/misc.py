from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from school_management.models import SchoolStaff
from school_management.serializers import SchoolStaffSerializer, PublicSchoolStaffSerializer, GroupSerializer
from school_management.permissions import IsSuperuserOrReadOnly


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SchoolStaffViewSet(viewsets.ModelViewSet):
    queryset = SchoolStaff.objects.all()
    serializer_class = SchoolStaffSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PublicSchoolStaffSerializer
        return SchoolStaffSerializer
