from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from school_management.models import SchoolStaff, Subject, Teacher, Student
from school_management.serializers import (SchoolStaffSerializer,GroupSerializer, TeacherSerializer,
                                           StudentSerializer, SubjectSerializer)
from school_management.permissions import IsSuperuserOrReadOnly
from rest_framework.permissions import IsAuthenticated


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class SchoolStaffViewSet(viewsets.ModelViewSet):
    queryset = SchoolStaff.objects.all()
    serializer_class = SchoolStaffSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'subjects', 'hired_date']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'birth_date']

    def list(self, request, *args, **kwargs):
        grade = request.query_params.get('grade', None)

        if grade:
            """Shu grade ga tegishli barcha studentlarni chiqarish"""
            students = self.queryset.filter(grade=grade)
            serializer = self.get_serializer(students, many=True)
            return Response(serializer.data)

        else:
            """Mavjud barcha grade larni chiqaradi.
               Takrorlanganlarini olib tashlaydi ['11-A', '11-B']
            """
            grades = self.queryset.values_list('grade', flat=True).distinct()
            return Response({'grades': list(grades)})


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


