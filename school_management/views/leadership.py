from rest_framework import viewsets

from school_management.permissions import IsSuperuserOrReadOnly
from school_management.models import LeaderShip
from school_management.serializers import LeaderShipSerializer


class LeaderShipViewSet(viewsets.ModelViewSet):
    queryset = LeaderShip.objects.all()
    serializer_class = LeaderShipSerializer
    permission_classes = [IsSuperuserOrReadOnly]
