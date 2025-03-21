from rest_framework import serializers
from school_management.models import Schedule, Subject, BellSchedule


class ScheduleSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)

    class Meta:
        model = Schedule
        fields = ['id', 'grade', 'shift', 'weekday', 'subjects']


class BellScheduleSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = BellSchedule
        fields = ['id', 'shift', 'start_time', 'end_time', 'break_time']