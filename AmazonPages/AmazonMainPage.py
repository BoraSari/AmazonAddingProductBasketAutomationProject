from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonMainPage:


  def __init__(self,driver):
     self.driver = driver
     self.search_box = (By.ID,"twotabsearchtextbox")




  def search_product(self,product):
   self.driver.find_element(*self.search_box).send_keys(product,Keys.ENTER)


   