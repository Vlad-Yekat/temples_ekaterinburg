from django.urls import resolve
from django.test import TestCase
from core.views import index


class IndexPageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
