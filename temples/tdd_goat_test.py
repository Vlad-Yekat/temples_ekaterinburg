"""
TDD functional test first
"""
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_start_page(self):
        self.browser.get('http://127.0.0.1:8080')

        assert 'Храмы' in self.browser.title


if __name__ == '__main__':
    unittest.main(warnings='ignore')
