"""
Selenium browser object creation with methods to completely run through
process of searching for a product and adding it to the cart.
"""

# Use of manual sleeps unfortunately needed in certain methods due to
# inconsistency of Selenium expected_conditions behavior with Amazon.
# A custom exception class will be needed to address this.

import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import config

class AmazonProductFinder():
    """
    Create Selenium browser object based off of user browser choice.
    Executes search and add-to-cart of user's product search.
    """
    def __init__ (self, browser, website_url, product_search):
        """
        Accept 3 parameters: browser type, website URL and product to search.
        Create Selenium driver object, browse to website URL on specified
        browser.
        """
        self.browser = browser
        self.website_url = website_url.lower()
        self.product_search = product_search.lower()

        if 'chrome' in self.browser:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            self.web_driver = webdriver.Chrome(chrome_options=options)
        elif 'firefox' in self.browser:
            self.web_driver = webdriver.Firefox()
        else:
            self.web_driver = webdriver.Safari()
            self.web_driver.maximize_window()

        self.web_driver.get(website_url)
        self.wait = WebDriverWait(self.web_driver, 20)

    def user_login(self):
        """
        Log into amazon. This method is UNUSED for now as logging in
        via Selenium requires granting authentication permission via email.
        """
        self.web_driver.find_element(By.XPATH,
            "//*[@id='nav-link-accountList']").click()
        self.web_driver.find_element(
            By.XPATH, "//*[@id='ap_email']").send_keys(config.USERNAME,
            Keys.ENTER)
        self.web_driver.find_element(By.XPATH,
            "//*[@id='ap_password']").send_keys(config.PASSWORD, Keys.ENTER)

    def search_for_product(self):
        """Search for the product that was specified in the user prompt."""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='twotabsearchtextbox']"))).send_keys(
            self.product_search, Keys.ENTER)
        if self.check_search_validity() is not None:
            print("ERROR! Search did not yield results. Exiting program.")
            self.close_browser_window()
            sys.exit()

    def check_search_validity(self):
        """Verify that the search yielded at least one result."""
        try:
            self.no_results = (self.web_driver.find_element(By.XPATH,
                    "//*[contains(text(), 'No results')]"))
            return self.no_results
        except NoSuchElementException:
            pass

    def adjust_sort_order(self):
        """Adjust search filter to filter by highest average review."""
        # Loop logic needed here as occasionally Selenium will not find xpath
        # despite xpath exiting in page XML.
        while True:
            try:
                sleep(5)
                self.web_driver.find_element(By.XPATH,
                    "//*[@id='a-autoid-0-announce']").click()
                sleep(3)
                self.web_driver.find_element(By.XPATH,
                    "//*[@id='s-result-sort-select_3']").click()
                break
            except NoSuchElementException:
                continue

    def go_to_product_page(self):
        """Click on first result for product page."""
        # XML here is dynamic and the search result ID varies depending on
        # whether or not the item is tagged as a "best seller"
        sleep(5)
        best_seller = False
        try:
            product_result = self.web_driver.find_element(By.XPATH,
                "//*[@data-cel-widget='search_result_1']//img")
        except NoSuchElementException:
            best_seller = True
        if best_seller:
            product_result = self.web_driver.find_element(By.XPATH,
                "//*[@data-cel-widget='search_result_2']//img")
        product_result.click()

    def add_product_to_cart(self):
        """Add product to cart and decline extended warranty if present."""
        try:
            sleep(5)
            self.web_driver.find_element(By.XPATH,
                "//*[@id='add-to-cart-button']").click()
            sleep(5)
            self.decline_warranty_offer()
        except NoSuchElementException:
            print("ERROR! Item does not have an 'add to cart' button.")
            print("Please re-run script and choose a product that can be "
                "added to an Amazon cart.")
            print("Exiting program.")
            sys.exit()

    def decline_warranty_offer(self):
        """Decline warranty offer pop up."""
        try:
            # Amazon does not always present warranty dialogue for all products
            # Javascript neccessary as there is a Selenium bug with modal interactions
            decline_warranty_offer = self.web_driver.find_element(By.XPATH,
                "/html/body/div[4]/div/div/header/button")
            self.web_driver.execute_script("arguments[0].click();",
                decline_warranty_offer)
        except NoSuchElementException:
            pass

    def go_to_cart(self):
        """Navigate to shopping cart."""
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH,
                "//*[@id='hlb-view-cart-announce']"))).click()
        except TimeoutException:
            sidesheet_view = True
        if sidesheet_view:
            try:
                self.wait.until(ec.element_to_be_clickable((By.XPATH,
                    "//*[@id='attach-sidesheet-view-cart-button']/span/input"
                    ))).click()
            except NoSuchElementException:
                print("Unexpected XML layout. Closing program.")
                sys.exit()

    def close_browser_window(self):
        """Issue quit against web driver object."""
        self.web_driver.quit()
