from pyclbr import Class

from pycparser.ply.yacc import debug_file
from selenium.webdriver.common.by import By

class ProductResultPage:

    def __init__(self,driver):
        self.driver = driver
        self.buying_options_section= (By.XPATH,"//img[@src='https://m.media-amazon.com/images/I/61beiSXOXVL._AC_UL320_.jpg'][1]")




    def click_product_image(self):
       self.driver.find_element(*self.buying_options_section).click()




