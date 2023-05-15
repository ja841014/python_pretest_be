from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from rest_framework.test import APITestCase, APIClient
from PretestBE.models import User
from rest_framework import status

import json


class PointAPITests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user1 = User.objects.create(name='User 1')
        self.user2 = User.objects.create(name='User 2')

    def test_create_user(self):
        url = reverse('users')
        data = {
            'name': 'Test User'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 3)

    def test_get_all_users(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data['users'][0]['name'], 'User 1')
        self.assertEqual(response_data['users'][1]['name'], 'User 2')

    def test_modify_positive_points(self):
        url = reverse('points')
        data = {'id': self.user1.id, 'point': 5}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.point, 5)


    def test_modify_negative_points(self):
        url = reverse('points')
        data = {'id': self.user1.id, 'point': -5}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.point, 0)