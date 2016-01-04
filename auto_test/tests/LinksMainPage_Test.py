import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import nose
from nose.plugins.attrib import attr
from selenium import webdriver
from base.BaseTest import BaseTest
from pages.MainPage import MainPage
from pages.CoachingForWomenPage import CoachingForWomenPage
from pages.CoachingForMenPage import CoachingForMenPage
from pages.CertificationPage import CertificationPage

#import HTMLTestRunner
from base.TestSettings import Test_Settings as s

class LinksMainPage(BaseTest, unittest.TestCase):

    def setUp(self):
        super(LinksMainPage, self).setUp()
        self.page = MainPage(self.driver, root_uri=s['root_url'])
        self.page.get(MainPage._page_url)

    @attr(priority='high')
    def testclick_coaching_for_women(self):
        self.page._coaching_for_women_img.click()
        self.assertIn(CoachingForWomenPage._page_title, self.page.w.title)
        # verify we are on Search Page by checking page title
        self.assertIn(CoachingForWomenPage._page_url, self.page.w.current_url)

    @attr(priority='high')
    def testclick_coaching_for_men(self):
        self.page._coaching_for_men_img.click()
        self.assertIn(CoachingForMenPage._page_title, self.page.w.title)
        self.assertIn(CoachingForMenPage._page_url, self.page.w.current_url)

    @attr(priority='high')
    def testclick_certification(self):
        self.page._certification_img.click()
        self.assertIn(CertificationPage._page_title, self.page.w.title)
        self.assertIn(CertificationPage._page_url, self.page.w.current_url)

    def tearDown(self):
        super(LinksMainPage, self).tearDown()


if __name__ == "__main__":
    nose.main()
