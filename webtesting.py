from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from selenium.common.exceptions import NoSuchElementException

class TutorialNinjaUITests(unittest.TestCase):
    def __init__(self, methodName='test_1_item_verification', url="https://tutorialsninja.com/demo/"):
        super().__init__(methodName)
        self.url = url

    # Setup method to initialize the WebDriver and navigate to the target URL
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.get(self.url)

    # Test to verify the visibility of specific items on the homepage
    def test_1_item_verification(self):
        try:
            macbook = self.web.find_element(By.XPATH, "//a[contains(text(), 'MacBook')]")
            iphone = self.web.find_element(By.XPATH, "//a[contains(text(), 'iPhone')]")
            apple_cinema = self.web.find_element(By.XPATH, "//a[contains(text(), 'Apple Cinema 30')]")
            canon = self.web.find_element(By.XPATH, "//a[contains(text(), 'Canon EOS 5D')]")
            self.assertTrue(macbook.is_displayed())
            self.assertTrue(iphone.is_displayed())
            self.assertTrue(apple_cinema.is_displayed())
            self.assertTrue(canon.is_displayed())
        except NoSuchElementException as e:
            self.fail(f"Test failed: An expected item is not found on the homepage. Details: {e}")

    # Test to verify the visibility of product descriptions and the Add to Cart button
    def test_2_description_verification(self):
        try:
            canon_description = self.web.find_element(By.XPATH, "//*[contains(text(), \"Canon's press material for the EOS\")]")
            add_to_cart = self.web.find_element(By.XPATH, "//*[contains(text(), 'Add to Cart')]")
            self.assertTrue(canon_description.is_displayed())
            self.assertTrue(add_to_cart.is_displayed())
        except NoSuchElementException as e:
            self.fail(f"Test failed: An expected item or button is not found on the homepage. Details: {e}")

    # Test to verify the visibility of header links like My Account, Wishlist, and Checkout
    def test_3_header_links_visibility(self):
        try:
            contact_number = self.web.find_element(By.XPATH, "//a[contains(text(), '123456789') or contains(text(), 'Contact')]")
            my_account = self.web.find_element(By.XPATH, "//a[contains(text(), 'My Account')]")
            wishlist = self.web.find_element(By.XPATH, "//a[contains(text(), 'Wish List')]")
            shopping_cart = self.web.find_element(By.XPATH, "//a[@title='Shopping Cart']")
            checkout = self.web.find_element(By.XPATH, "//a[@title='Checkout' or contains(@href, 'checkout')]")
            self.assertTrue(contact_number.is_displayed())
            self.assertTrue(my_account.is_displayed())
            self.assertTrue(wishlist.is_displayed())
            self.assertTrue(shopping_cart.is_displayed())
            self.assertTrue(checkout.is_displayed())
        except NoSuchElementException as e:
            self.fail(f"Test failed: An expected header link is not found on the homepage. Details: {e}")

    # Test to search for "laptop" and verify the results or no results message
    def test_4_search_laptop(self):
        search_bar = self.web.find_element(By.NAME, "search")
        search_bar.clear()
        search_bar.send_keys("laptop")
        search_button = self.web.find_element(By.CLASS_NAME, "btn-default")
        search_button.click()

        try:
            results = self.web.find_elements(By.CLASS_NAME, "product-thumb")
            if results:
                return
            else:
                no_result_message = self.web.find_element(By.XPATH, "//*[contains(text(), 'There is no product that matches the search criteria.')]")
                self.assertTrue(no_result_message.is_displayed(), "No results message is not displayed.")
                return
        except NoSuchElementException as e:
            self.fail(f"Test failed: 'No results' message or product results not displayed as expected for 'laptop' search. Details: {e}")

    # Test to search for "testing" within the scanner dropdown and verify the results
    def test_5_search_testing_with_scanner_dropdown(self):
        search_url = "https://tutorialsninja.com/demo/index.php?route=product/search&search=testing&category_id=31"
        self.web.get(search_url)

        try:
            results = self.web.find_elements(By.CLASS_NAME, "product-thumb")
            if results:
                return
            else:
                no_result_message = self.web.find_element(By.XPATH, "//*[contains(text(), 'There is no product that matches the search criteria.')]")
                self.assertTrue(no_result_message.is_displayed(), "No results message is not displayed.")
        except NoSuchElementException as e:
            self.fail(f"Test failed: 'results not displayed as expected for 'testing' with 'scanner' search. Details: {e}")

    # Test to add an item to the cart and proceed to checkout
    def test_6_checkout_item(self):
        search_bar = self.web.find_element(By.NAME, "search")
        search_bar.clear()
        search_bar.send_keys("MacBook")
        search_button = self.web.find_element(By.CLASS_NAME, "btn-default")
        search_button.click()

        try:
            macbook = self.web.find_element(By.LINK_TEXT, "MacBook")
            macbook.click()
            add_to_cart_button = self.web.find_element(By.ID, "button-cart")
            add_to_cart_button.click()
            cart_button = self.web.find_element(By.ID, "cart")
            cart_button.click()
            checkout_button = self.web.find_element(By.LINK_TEXT, "Checkout")
            checkout_button.click()
        except NoSuchElementException as e:
            self.fail(f"Checkout process failed: {e}")

    # Tear down method to close the WebDriver after tests
    def tearDown(self):
        self.web.quit()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
