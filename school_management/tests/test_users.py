from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class AnonymousUserTestCase(APITestCase):
    def test_can_view_objects(self):
        urls = [
            reverse('leadership-list'),
            reverse('schoolstaff-list'),
            reverse('schedule-list'),
            reverse('bellschedule-list'),
            reverse('clubschedule-list'),
            reverse('event-list'),
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_view_objects(self):
        urls = [
            reverse('teacher-list'),
            reverse('student-list'),
            reverse('subject-list'),
            reverse('group-list')
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
