import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v85.target import detach_from_target
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver
from AmazonPages.Datas import base_url
from  AmazonPages.AmazonMainPage import AmazonMainPage
from  AmazonPages.ProductDetailsPage import  ProductDetails
from  AmazonPages.ProductResultPage import ProductResultPage

@pytest.fixture
def driver():
 driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 driver.get(base_url)
 driver.maximize_window()
 driver.implicitly_wait(15)
 yield driver
 driver.quit()



def test_product_search(driver):
  main_page = AmazonMainPage(driver)
  main_page.search_product("Gaming Laptop")


def test_click_product(driver):
   main_page = AmazonMainPage(driver)
   main_page.search_product("Gaming Laptop")
   result_page = ProductResultPage(driver)
   details_page = ProductDetails(driver)
   details_page.accept_cookie_section()
   result_page.click_product_image()

   ##Model number check
   product_model_number = details_page.get_model_number_of_product()
   actual_text_model_number_of_product = details_page.get_model_number_of_product_text()
   expected_result_model_number = "7Z595EA"
   assert product_model_number.is_displayed()
   assert expected_result_model_number.__eq__(actual_text_model_number_of_product), f"f expected_result = {expected_result_model_number},actual_result = {actual_text_model_number_of_product}"


def test_adding_product_in_basket(driver):
  main_page = AmazonMainPage(driver)
  main_page.search_product("Gaming Laptop")
  details_page = ProductDetails(driver)
  details_page.accept_cookie_section()
  result_page = ProductResultPage(driver)
  result_page.click_product_image()
  details_page.click_add_to_card_button()

  ##Product Price
  adding_basket_message = details_page.get_adding_basket_message()
  adding_basket_message_text = details_page.get_adding_basket_message_text()
  expected_message = "Sepete eklendi"
  assert adding_basket_message.is_displayed()
  assert  expected_message.__eq__(adding_basket_message),f"f expected_result = {expected_message},actual_result = {adding_basket_message}"

  ##Count Of Basket Number
  basket_number = details_page.get_count_of_product_for_basket()
  basket_number_text = details_page.get_count_of_product_for_basket_text()
  print(basket_number_text)
  expected_basket_count_number = "1"

  assert  basket_number.is_displayed()
  assert  expected_basket_count_number.__contains__(basket_number_text),f"f expected_result = {expected_basket_count_number},actual_result = {basket_number}"











