from rest_framework import serializers

from .models import LeaderShip, SchoolStaff


class LeaderShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderShip
        fields = '__all__'
        depth = 1  # user obyektini ichidagi hamma field keladi

    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


class SchoolStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStaff
        fields = '__all__'
        depth = 1  # user obyektini ichidagi hamma field keladi

    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

