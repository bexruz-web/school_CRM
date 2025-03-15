from rest_framework import viewsets

from school_management.models import SchoolStaff
from school_management.serializers import SchoolStaffSerializer
from school_management.permissions import IsStaffOrReadOnly


class SchoolStaffViewSet(viewsets.ModelViewSet):
    queryset = SchoolStaff.objects.all()
    serializer_class = SchoolStaffSerializer
    permission_classes = [IsStaffOrReadOnly]

