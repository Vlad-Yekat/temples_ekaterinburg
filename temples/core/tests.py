from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from core.views import index


class IndexPageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_root_page_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('core/index.html')
        self.assertEqual(response.content.decode(), expected_html)