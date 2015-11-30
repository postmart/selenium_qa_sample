from page_objects import PageObject, PageElement
#from selenium import webdriver

class SearchPage(PageObject):

        _page_title = 'Search | Precision Nutrition'
        _page_url = '/search?q='
        _search_wrapper_area = PageElement(class_name='gsc-above-wrapper-area')
        _search_results = PageElement(class_name='gsc-webResult')
        _search_results_selenium = 'gsc-webResult'

        