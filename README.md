Amazon Product Details Verification Automation Project
Project Overview
This project provides an automated test suite for verifying key functionalities on the Amazon e-commerce website, specifically focusing on product search, product details verification, and the "add to cart" process. It covers searching for a specific product, navigating to its details page to verify information like the model number, adding the product to the shopping basket, and confirming the successful addition and the updated item count in the basket. Developed using Python, Selenium WebDriver, and PyTest, it adheres to best practices such as the Page Object Model (POM) and external data management.

Project Goal
The main objectives of this project are to:

Automate the search for a specific product on Amazon.

Navigate to the product's detail page from the search results.

Verify critical product information, such as the model number, on the detail page.

Automate the process of adding the selected product to the shopping basket.

Confirm the successful "added to cart" message after the product is added.

Validate that the product count in the shopping basket updates correctly.

Showcase practical application of Python, Selenium WebDriver, and PyTest for e-commerce test automation, emphasizing product information validation and cart operations.

Technologies Used
Programming Language: Python

Test Automation Framework: Selenium WebDriver

Testing Framework: PyTest

Browser Driver Management: WebDriverManager (for Chrome)

Design Pattern: Page Object Model (POM)

Data Handling: External Datas module for test data (e.g., base_url, selected_product, expected_texts).

Setup and Run Instructions
To set up and run this project locally, follow these steps:

Clone the Repository:

git clone https://github.com/BoraSari/AmazonProductDetailsVerificationAutomation.git
cd AmazonProductDetailsVerificationAutomation

(Note: Please replace BoraSari with your actual GitHub username if different. Adjust the repository name if it's different in your actual GitHub setup.)

Create and Activate Virtual Environment (Recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Dependencies:

pip install -r requirements.txt

(You'll need a requirements.txt file in your project. You can generate it by running pip freeze > requirements.txt after installing all necessary libraries.)
(Common libraries to include: selenium, pytest, webdriver-manager)

Configure Test Data:
Ensure your AmazonPages/Datas.py file contains the correct and up-to-date test data such as base_url and selected_product.

Run the Tests:

pytest -v

To run specific tests:

pytest -k "test_product_search" -v
pytest -k "test_click_product" -v
pytest -k "test_adding_product_in_basket" -v

Test Coverage and Scenarios
This project covers the following key scenarios for Amazon's product details and cart operations:

test_product_search:

Description: Verifies that a specific product can be successfully searched on the Amazon website.

Flow: Navigates to the Amazon homepage, enters the selected_product into the search bar, and initiates the search.

test_click_product:

Description: Validates the navigation to the product details page from search results and verifies the product's model number.

Flow: Performs a product search, accepts cookie settings, clicks on the product image from the results, and asserts that the displayed model number matches the expected_result_model_number ("7Z595EA").

test_adding_product_in_basket:

Description: Tests the functionality of adding a product to the shopping basket and verifies the successful addition message and the updated basket item count.

Flow: Performs a product search, accepts cookie settings, clicks on the product image, clicks the "Add to Cart" button, asserts that the "Sepete eklendi" (Added to cart) message is displayed, and finally asserts that the basket count is "1".

Screenshots/GIFs
(Please add screenshots or GIFs here demonstrating the test execution for various scenarios, such as product search, product details page with model number, the "added to cart" message, and the updated basket count, to visually showcase the project's functionality.)

License
This project is licensed under the MIT License - see the LICENSE file for details.

Amazon Ürün Detayları Doğrulama Otomasyon Projesi
Projeye Genel Bakış
Bu proje, Amazon e-ticaret web sitesindeki temel işlevsellikler için otomatik bir test paketi sunar ve ürün arama, ürün detayları doğrulama ve "sepete ekleme" sürecine odaklanır. Belirli bir ürünü arama, detay sayfasına giderek model numarası gibi bilgileri doğrulama, ürünü alışveriş sepetine ekleme ve başarılı ekleme ile sepetin güncellenen ürün sayısını onaylama adımlarını kapsar. Python, Selenium WebDriver ve PyTest kullanılarak geliştirilen bu proje, Page Object Model (POM) ve harici veri yönetimi gibi en iyi uygulamalara uyar.

Proje Amacı
Bu projenin temel hedefleri şunlardır:

Amazon'da belirli bir ürün aramasını otomatikleştirmek.

Arama sonuçlarından ürünün detay sayfasına gitmek.

Detay sayfasında ürünün model numarası gibi kritik bilgileri doğrulamak.

Seçilen ürünü alışveriş sepetine ekleme sürecini otomatikleştirmek.

Ürün eklendikten sonra başarılı "sepete eklendi" mesajını onaylamak.

Alışveriş sepetindeki ürün sayısının doğru bir şekilde güncellendiğini doğrulamak.

Ürün bilgisi doğrulama ve sepet işlemleri vurgusuyla e-ticaret test otomasyonu için Python, Selenium WebDriver ve PyTest'in pratik uygulamasını sergilemek.

Kullanılan Teknolojiler
Programlama Dili: Python

Test Otomasyon Çerçevesi: Selenium WebDriver

Test Çerçevesi: PyTest

Tarayıcı Sürücüsü Yönetimi: WebDriverManager (Chrome için)

Tasarım Deseni: Page Object Model (POM)

Veri Yönetimi: Test verileri (örn: base_url, selected_product, expected_texts) için harici Datas modülü.

Kurulum ve Çalıştırma Talimatları
Bu projeyi yerel olarak kurmak ve çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

git clone https://github.com/BoraSari/AmazonProductDetailsVerificationAutomation.git
cd AmazonProductDetailsVerificationAutomation

(Not: Lütfen BoraSari yerine gerçek GitHub kullanıcı adınızı yazın. GitHub'daki gerçek kurulumunuz farklıysa depo adını ayarlayın.)

Sanal Ortam Oluşturma ve Etkinleştirme (Önerilir):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux'ta:
source venv/bin/activate

Bağımlılıkları Yükle:

pip install -r requirements.txt

(Projenizde bir requirements.txt dosyası bulunması gerekmektedir. Gerekli tüm kütüphaneleri kurduktan sonra pip freeze > requirements.txt komutuyla oluşturabilirsiniz.)
(Eklenecek yaygın kütüphaneler: selenium, pytest, webdriver-manager)

Test Verilerini Yapılandırın:
AmazonPages/Datas.py dosyanızın base_url ve selected_product gibi doğru ve güncel test verilerini içerdiğinden emin olun.

Testleri Çalıştırın:

pytest -v

Belirli testleri çalıştırmak için:

pytest -k "test_product_search" -v
pytest -k "test_click_product" -v
pytest -k "test_adding_product_in_basket" -v

Test Kapsamı ve Senaryoları
Bu proje, Amazon'un ürün detayları ve sepet işlemleri için aşağıdaki temel senaryoları kapsar:

test_product_search:

Açıklama: Belirli bir ürünün Amazon web sitesinde başarılı bir şekilde aranabildiğini doğrular.

Akış: Amazon ana sayfasına gider, selected_product'ı arama çubuğuna girer ve aramayı başlatır.

test_click_product:

Açıklama: Arama sonuçlarından ürün detay sayfasına navigasyonu doğrular ve ürünün model numarasını kontrol eder.

Akış: Bir ürün araması yapar, çerez ayarlarını kabul eder, sonuçlardan ürün görseline tıklar ve görüntülenen model numarasının expected_result_model_number ("7Z595EA") ile eşleştiğini doğrular.

test_adding_product_in_basket:

Açıklama: Bir ürünün alışveriş sepetine eklenmesi işlevselliğini test eder ve başarılı ekleme mesajı ile güncellenen sepet ürün sayısını doğrular.

Akış: Bir ürün araması yapar, çerez ayarlarını kabul eder, ürün görseline tıklar, "Sepete Ekle" düğmesine tıklar, "Sepete eklendi" mesajının görüntülendiğini doğrular ve son olarak sepet sayısının "1" olduğunu doğrular.

Ekran Görüntüleri/GIF'ler
![image](https://github.com/user-attachments/assets/205901a3-cbf2-46b1-8236-b8472b0819f7)

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - daha fazla ayrıntı için LICENSE dosyasına bakın.
