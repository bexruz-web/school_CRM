from rest_framework import viewsets

from school_management.permissions import IsSuperuserOrReadOnly
from school_management.models import LeaderShip
from school_management.serializers import LeaderShipSerializer, PublicLeaderShipSerializer


class LeaderShipViewSet(viewsets.ModelViewSet):
    queryset = LeaderShip.objects.all()
    serializer_class = LeaderShipSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PublicLeaderShipSerializer
        return LeaderShipSerializer



