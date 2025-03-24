from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

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

    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'subjects', 'hired_date']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'birth_date']

    def list(self, request, *args, **kwargs):
        grade = request.query_params.get('grade', None)

        queryset = self.queryset
        if grade:
            queryset = queryset.filter(grade=grade)
        else:
            queryset = self.queryset.values_list('grade', flat=True).distinct()
            return Response({'grades': queryset})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


