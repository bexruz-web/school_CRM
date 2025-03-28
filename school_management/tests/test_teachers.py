from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school_management.models import Teacher


class TeacherTestCase(APITestCase):
    fixtures = ['groups', 'users', 'subjects', 'teachers']

    def setUp(self):
        teacher = Teacher.objects.first()
        self.assertIsNotNone(teacher, 'Teacher topilmadi')
        self.assertIsNotNone(teacher.user, 'Teacher useri topilmadi')
        self.client.force_authenticate(user=teacher.user)

    def test_can_create_event(self):
        url = reverse('event-list')
        data = {
            'title': 'Matematika Olimpiadasi',
            'description': 'Maktab matematika olimpiadasi',
            'date': '2025-03-04'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_update_objects(self):
        """Teacherlar post, patch, delete qila olmaydi: is_superuser=False !!!
           faqatgina ko'ra(get) oladi admin panelda"""
        update_data_list = [
            (reverse('leadership-detail', args=[1]), {'position': 'Vice Principal'}),
            # (reverse('teacher-detail', args=[1]), {'phone_number': '4323232322', 'bio': 'Updated bio'}),
        ]

        for url, data in update_data_list:
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
