"""
TDD
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main_test():
    """
    TDD
    :return:
    """
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://127.0.0.1:8080')

    assert 'framework' in browser.title


if __name__ == '__main__':
    main_test()
