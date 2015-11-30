from selenium import webdriver
from TestSettings import Test_Settings as s
class BaseTest(object):

  def setUp(self):
    if s['Browser'].lower() == "firefox":
      self.driver = webdriver.Firefox()
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)
    elif s['Browser'].lower() == "chrome":
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)
    elif s['Browser'].lower() == "ie": 
      self.driver = webdriver.Ie()
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)
    elif s['Browser'].lower() == "phantomjs": 
      self.driver = webdriver.PhantomJS()
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)
    else:
      raise Exception("Set Up <Browser> in TestSettings file. Supported browsers: Firefox, Chrome, IE, PhantomJS")


  def tearDown(self):
      self.driver.quit()
