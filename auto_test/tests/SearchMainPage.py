import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from selenium import webdriver
from base.BaseTest import BaseTest
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
import HTMLTestRunner
from base.TestSettings import Test_Settings as s

class SearchMainPage(BaseTest, unittest.TestCase):

    def setUp(self):
        super(SearchMainPage, self).setUp()
        self.page = MainPage(self.driver, root_uri=s['root_url'])
        self.page.get(MainPage._page_url)
        
       
    def testsearchMain(self):
        search_term = ""
        self.page._search_query_locator = search_term
        self.page._search_submit.click()

        # verify we are on Search Page by checking page title
        self.assertIn(SearchPage._page_title, self.page.w.title)

        # verify that there are any search results (more than 0)
        results = self.page.w.find_elements_by_class_name(SearchPage._search_results_selenium)
        self.assertGreater(len(results), 0)


    def tearDown(self):
        #self.driver.quit()
        super(SearchMainPage, self).tearDown()

if __name__ == "__main__":
    test = unittest.TestLoader().loadTestsFromTestCase(SearchMainPage)
    #unittest.TextTestRunner().run(test)
    outfile = open("../reports/SearchPage.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='SearchPage Test Report'
                                )
    runner.run(test)
