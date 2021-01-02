from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import City, Country
from users.models import CustomUser


class CityAPITest(APITestCase):

    def test_city_index(self):
        url = reverse('api:city_index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_create(self):
        url = reverse('api:city_index')
        data = {'name': 'Paris'}
        test_user = CustomUser.objects.create_superuser(username='test_user', password='test_password')
        self.client.login(username=test_user, password='test_password')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.city = City.objects.get(pk=1)
        self.assertEqual(self.city.name, 'Paris')


class CountryAPITest(APITestCase):

    def test_country_index(self):
        url = reverse('api:country_index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)