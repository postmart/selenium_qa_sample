from page_objects import PageObject, PageElement

class MainPage(PageObject):

        _page_title = 'Nutrition Coaching and Certification | Precision Nutrition'
        _page_url = '/'
        _get_started_button = PageElement(class_name='button_blue')
        _sing_in_button = PageElement(class_name='sign_in')
        _search_query_locator = PageElement(name='q')
        _search_submit = PageElement(xpath='//button[@type="submit"]')
        _blog_link = PageElement(xpath='//a[@href="/blog"]')



