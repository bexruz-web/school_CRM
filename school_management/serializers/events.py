from rest_framework import serializers
from school_management.models import Event, EventPhoto


class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = ['image']


class EventSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False)
    photos_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'photos', 'photos_url']

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        event = Event.objects.create(**validated_data)

        for photo_data in photos_data:
            EventPhoto.objects.create(event=event, photos=photo_data)

        return event

    def update(self, instance, validated_data):
        photos_data = validated_data.pop('photos', None)

        instance = super().update(instance, validated_data)

        if photos_data is not None:
            for photo_data in photos_data:
                EventPhoto.objects.create(event=instance, photos=photo_data)

        return instance

    def get_photos_url(self, obj):
        return [photo.photos.name for photo in obj.event_photos.all()]
