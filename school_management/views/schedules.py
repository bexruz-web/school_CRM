from rest_framework import viewsets
from rest_framework.response import Response

from school_management.permissions import IsSuperuserOrReadOnly
from school_management.serializers import ScheduleSerializer, BellScheduleSerializer
from school_management.models import Schedule, BellSchedule


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def list(self, request, *args, **kwargs):
        grade = request.query_params.get('grade', None)

        queryset = self.queryset
        if grade:
            queryset = queryset.filter(grade=grade)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BellScheduleViewSet(viewsets.ModelViewSet):
    queryset = BellSchedule.objects.all()
    serializer_class = BellScheduleSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def list(self, request, *args, **kwargs):
        shift = request.query_params.get('shift', None)

        queryset = self.queryset
        if shift:
            queryset = queryset.filter(shift=shift)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
