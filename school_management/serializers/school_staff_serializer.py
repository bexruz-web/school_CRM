from django.contrib.auth.models import Group
from rest_framework import serializers
from school_management.models import SchoolStaff
from school_management.serializers import CustomUserSerializer, PublicCustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class SchoolStaffSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, write_only=True)
    user = CustomUserSerializer()

    class Meta:
        model = SchoolStaff
        fields = ['id', 'user', 'position', 'phone_number', 'bio', 'hired_date', 'photo', 'groups']

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        staff = SchoolStaff.objects.create(user=user, **validated_data)

        if groups_data:
            user.groups.add(*groups_data)

        return staff

    def update(self, instance, validated_data):
        groups_data = validated_data.pop('groups', None)
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)
            user_instance.save()

        if groups_data is not None:
            instance.user.groups.set(groups_data)

        return super().update(instance, validated_data)


class PublicSchoolStaffSerializer(serializers.ModelSerializer):
    user = PublicCustomUserSerializer()

    class Meta:
        model = SchoolStaff
        fields = ['id', 'user', 'position', 'bio', 'photo']