from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from school_management.models import LeaderShip


class LeadershipTests(APITestCase):
    fixtures = ['groups', 'users', 'leaderships', 'teachers', 'subjects', 'schoolstaffs', 'students', 'schedules']

    def setUp(self):
        leadership = LeaderShip.objects.first()
        self.assertIsNotNone(leadership, 'Leadership topilmadi')
        self.assertIsNotNone(leadership.user, 'Leadership useri topilmadi')
        self.client.force_authenticate(user=leadership.user)

    def test_leadership_can_view_all_lists(self):
        urls = [
            reverse('group-list'),
            reverse('schoolstaff-list'),
            reverse('teacher-list'),
            reverse('student-list'),
            reverse('subject-list'),
            reverse('schedule-list'),
            reverse('bellschedule-list'),
            reverse('clubschedule-list'),
            reverse('event-list'),
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leadership_can_create_objects(self):
        data_list = [
            (reverse('teacher-list'), {
                'user': {'username': 'new_teacher', 'password': 'teacher_pass', 'role': 'teacher'},
                'groups': [1],
                'subjects': [1],
                'phone_number': '09876543234',
                'bio': 'str',
                'hired_date': '2021-01-01'}),
            (reverse('schoolstaff-list'), {
                'user': {'username': 'new_staff', 'password': 'staff_pass', 'role': 'staff'},
                'position': 'Librarian',
                'phone_number': '12342321',
                'bio': 'Kutubxonachi',
                'hired_date': '2022-05-10'}),
            (reverse('clubschedule-list'), {
                'name': 'Matematiklar',
                'subject': 2,
                'weekday': 'Du-Chor-Juma',
                'teacher': 1,
                'grades': '5-8',
                'start_time': '13:30:00',
                'end_time': '15:30:00',
                'students': 20}),
            (reverse('student-list'), {'full_name': 'Sardor Asqarov', 'grade': '11-B', 'birth_date': '2008-06-02'}),
            (reverse('subject-list'), {'name': 'Ona tili'}),
            (reverse('schedule-list'), {'grade': '11-B', 'shift': 1, 'subjects': [1,2,3,4,5], 'weekday': 'monday'}),
            (reverse('bellschedule-list'), {'shift': 1, 'start_time': '08:00:00', 'end_time': '08:45:00'}),
        ]
        for url, data in data_list:
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED, f'{response.json()}')

    def test_leadership_cannot_create_event(self):
        url = reverse('event-list')
        data = {'title': 'Yangi yil bayrami', 'date': '2025-12-31', 'description': 'Yangi yil bayrami o\'tkazildi'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_leadership_can_update_objects(self):
        update_data_list = [
            (reverse('leadership-detail', args=[1]), {'position': 'Vice Principal'}),
            (reverse('teacher-detail', args=[1]), {'phone_number': '4323232322', 'bio': 'Updated bio'}),
            (reverse('schoolstaff-detail', args=[1]), {'user': {'password': 'test_staff'}}),
            (reverse('student-detail', args=[1]), {'phone_number': '+998889876543'}),
            (reverse('schedule-detail', args=[1]), {'subjects': [3,2,4,5,1]}),
        ]

        for url, data in update_data_list:
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK, f'{response.json()}')

