from django.test import TestCase

from core.models import Country, City, District, Street, Address, Church, Tag, Comment


class CountryModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Country()
        first_item.name = 'Cyprus'
        first_item.save()
        second_item = Country()
        second_item.name = 'Greece'
        second_item.save()
        saved_items = Country.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Cyprus')
        self.assertEqual(second_saved_item.name, 'Greece')


class CityModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = City()
        first_item.name = 'Berlin'
        first_item.save()

        saved_items = City.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertNotEqual(saved_items.count(), 0)
        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'Berlin')
