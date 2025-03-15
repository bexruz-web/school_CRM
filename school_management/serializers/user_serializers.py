from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'role']

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

