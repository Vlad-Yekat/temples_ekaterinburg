from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import City, Country
from django.contrib.auth.models import User


class CityAPITest(APITestCase):

    def test_city_index(self):
        url = reverse('api:city_index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_create(self):
        url = reverse('api:city_index')
        data = {'name': 'Paris'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.city = City.objects.get(pk=1)
        self.assertEqual(self.city.name, 'Paris')


class CountryAPITest(APITestCase):

    def test_country_index(self):
        url = reverse('api:country_index')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)