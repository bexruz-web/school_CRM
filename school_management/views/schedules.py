from rest_framework import viewsets
from rest_framework.response import Response

from school_management.permissions import IsSuperuserOrReadOnly
from school_management.serializers import ScheduleSerializer, BellScheduleSerializer, ClubScheduleSerializer
from school_management.models import Schedule, BellSchedule, ClubSchedule


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def list(self, request, *args, **kwargs):
        grade = request.query_params.get('grade', None)

        queryset = self.get_queryset()
        if grade:
            queryset = queryset.filter(grade__startswith=grade)  # e.g. 11-A and 11-B

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BellScheduleViewSet(viewsets.ModelViewSet):
    queryset = BellSchedule.objects.all()
    serializer_class = BellScheduleSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ClubScheduleViewSet(viewsets.ModelViewSet):
    queryset = ClubSchedule.objects.all()
    serializer_class = ClubScheduleSerializer
    permission_classes = [IsSuperuserOrReadOnly]

