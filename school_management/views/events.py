from rest_framework import viewsets

from school_management.serializers import EventSerializer
from school_management.models import Event
from school_management.permissions import IsTeacherOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsTeacherOrReadOnly]

