from rest_framework import viewsets

from school_management.permissions import IsStaffOrReadOnly
from school_management.models import LeaderShip, SchoolStaff
from school_management.serializers import LeaderShipSerializer, PublicLeaderShipSerializer


class LeaderShipViewSet(viewsets.ModelViewSet):
    queryset = LeaderShip.objects.all()
    serializer_class = LeaderShipSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PublicLeaderShipSerializer
        return LeaderShipSerializer



