from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class ProductDetails:

    def __init__(self,driver):
     self.driver = driver
     self.model_number = (By.XPATH, "(//span[contains(text(),'7Z595EA')])[2]")
     self.buying_options = (By.XPATH,"//a[contains(text(),' Satın Alma Seçeneklerini Gör ')]")
     self.adding_basket_message = (By.XPATH,"//h1[@tabindex='-1']")
     self.adding_basket_button = (By.ID,"add-to-cart-button")
     self.count_of_product_in_basket= (By.CSS_SELECTOR,"span[class='nav-cart-count nav-cart-1 nav-progressive-attribute nav-progressive-content']")
     self.cookie_section = (By.ID,"sp-cc-accept")


    def accept_cookie_section(self):
     self.driver.find_element(*self.cookie_section).click()

    def get_model_number_of_product(self):
     return self.driver.find_element(*self.model_number)

    def get_model_number_of_product_text(self):
     return self.driver.find_element(*self.model_number).text

    def get_adding_basket_message(self):
     return self.driver.find_element(*self.adding_basket_message)

    def get_adding_basket_message_text(self):
     return self.driver.find_element(*self.adding_basket_message).text

    def click_add_to_card_button(self):
     self.driver.find_element(*self.adding_basket_button).click()


    def get_count_of_product_for_basket(self):

        WebDriverWait(self.driver,20).until(Ec.visibility_of_element_located(self.count_of_product_in_basket))
        return self.driver.find_element(*self.count_of_product_in_basket)


    def get_count_of_product_for_basket_text(self):
      WebDriverWait(self.driver,20).until(Ec.visibility_of_element_located(self.count_of_product_in_basket))
      return self.driver.find_element(*self.count_of_product_in_basket).text













