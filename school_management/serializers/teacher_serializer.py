from rest_framework import serializers
from school_management.models import Teacher
from .misc import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subjects', 'phone_number', 'photo', 'bio', 'hired_date']

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])
        user_data = validated_data.pop('user')
        groups_data = user_data.pop('groups', [])

        user = User.objects.create_user(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)

        if subjects_data:
            teacher.subjects.add(*subjects_data)

        if groups_data:
            user.groups.add(*groups_data)

        return teacher

    def update(self, instance, validated_data):
        subjects_data = validated_data.pop('subjects', None)
        user_data = validated_data.pop('user', None)
        groups_data = user_data.pop('groups', None)

        if user_data:
            user_intance = instance.user
            for attr, value in user_data.items():
                setattr(user_intance, attr, value)
            user_intance.save()

        if subjects_data is not None:
            instance.subjects.set(subjects_data)

        if groups_data is not None:
            instance.user.groups.set(groups_data)

        return super().update(instance, validated_data)
