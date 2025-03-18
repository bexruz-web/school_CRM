from rest_framework import serializers
from django.contrib.auth.models import Group
from school_management.models import Subject, Student
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, write_only=True)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'role', 'groups']

    def create(self, validated_data):
        password = validated_data.pop('password')  # parol olamiz
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PublicCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"




