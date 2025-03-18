from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from school_management.models import SchoolStaff, Subject, Teacher, Student
from school_management.serializers import (SchoolStaffSerializer, PublicSchoolStaffSerializer,
                                           GroupSerializer, TeacherSerializer, StudentSerializer, SubjectSerializer)
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


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsSuperuserOrReadOnly]



