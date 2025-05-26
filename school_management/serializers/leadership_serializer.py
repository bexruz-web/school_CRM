from rest_framework import serializers
from school_management.models import LeaderShip
from .misc import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LeaderShipSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = LeaderShip
        fields = ['id', 'user', 'position', 'phone_number', 'photo', 'bio', 'hired_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # User malumotlarini ajratamiz
        user = User.objects.create_user(**user_data)  # New User
        leadership = LeaderShip.objects.create(user=user, **validated_data)  # New Leadership
        return leadership

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            user_instance = instance.user
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            user_instance.save()

        return super().update(instance, validated_data)

