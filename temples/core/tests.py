from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from core.views import index


class IndexPageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_root_page_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertContains(response, '<title>Храмы Екатеринбурга</title>')
        self.assertTrue(response.content.endswith(b'</html>'))
