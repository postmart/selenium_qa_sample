import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from selenium import webdriver
from base.BaseTest import BaseTest
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
import nose
from nose.plugins.attrib import attr
from base.TestSettings import Test_Settings as s

class SearchMainPage(BaseTest, unittest.TestCase):

    def setUp(self):
        super(SearchMainPage, self).setUp()
        self.page = MainPage(self.driver, root_uri=s['root_url'])
        self.page.get(MainPage._page_url)

    @attr(priority='high')
    def testsearchMain(self):
        search_term = "lose weight"
        self.page._search_query_locator = search_term
        self.page._search_submit.click()

        # verify we are on Search Page by checking page title
        self.assertIn(SearchPage._page_title, self.page.w.title)

        # verify that there are any search results (more than 0)
        results = self.page.w.find_elements_by_class_name(SearchPage._search_results_selenium)
        self.assertGreater(len(results), 0)


    def tearDown(self):
        super(SearchMainPage, self).tearDown()

if __name__ == "__main__":
    nose.main()
