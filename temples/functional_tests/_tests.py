"""
TDD functional test first
test_goat
"""
from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class NewClientTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_start_page(self):
        self.browser.get(self.live_server_url)

        assert 'Храмы' in self.browser.title

    def test_main_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Храмы', self.browser.title)
        main_list = self.browser.find_element_by_class_name('main_list').text
        self.assertIn('Ганина', main_list)

        # Enter a text in search string
        search_input = self.browser.find_element_by_id('search')
        self.assertEqual(
            search_input.get_attribute('placeholder'),
            'Enter to search ...'
        )
        search_input.send_keys('Ekat')
        search_input.send_keys(Keys.ENTER)
        result = self.browser.find_element_by_id('result_list')
        rows_result = result.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == 'No result' for row in rows_result))
