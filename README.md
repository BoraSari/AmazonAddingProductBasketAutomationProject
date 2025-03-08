This project is an automation framework that tests the functionality of adding products to the basket on the Amazon platform. It uses Selenium, Pytest, and the Page Object Model (POM) design to ensure modular, reusable, and maintainable test scripts. The framework is designed to validate cart-related functionalities, including adding products to the basket and verifying price accuracy and basket updates.

🚀 Features
Add to Basket Automation: Automates adding products to the basket and validates the success of the operation.

Price Accuracy Tests: Ensures that the displayed price matches the product details and cart page.

Basket Update Verification: Verifies correct updates to quantities and total price within the cart.

Dynamic Wait Handling: Incorporates explicit waits to manage dynamically loaded web elements.

📋 Test Scenarios
Search and Add Product to Basket:

Validates that a user can search for and add a specific product to the basket.

Price Consistency Check:

Ensures that the price displayed in the basket is accurate and matches the product's detail page.

Basket Update Test:

Verifies the behavior of updating the quantity of items in the basket and reflects the correct total price.

🛠️ Technologies Used
Language: Python

Frameworks: Selenium, Pytest

Design Pattern: Page Object Model (POM)

Reporting: Pytest HTML

Browser: Chrome (via WebDriver)
