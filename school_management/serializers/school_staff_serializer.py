from django.contrib.auth.models import Group
from rest_framework import serializers
from school_management.models import SchoolStaff
from school_management.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class SchoolStaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = SchoolStaff
        fields = ['id', 'user', 'position', 'phone_number', 'bio', 'hired_date', 'photo']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        groups_data = user_data.pop('groups', [])

        user = User.objects.create_user(**user_data)
        staff = SchoolStaff.objects.create(user=user, **validated_data)

        if groups_data:
            user.groups.add(*groups_data)

        return staff

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', None)

        if user_data:
            user_instance = instance.user
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            user_instance.save()

        if groups_data is not None:
            instance.user.groups.set(groups_data)

        return super().update(instance, validated_data)
