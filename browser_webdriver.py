"""
Selenium browser object creation with methods to completely run through
process of searching for a product and adding it to the cart. 
"""

# Use of manual sleeps unfortunately needed in certain methods due to 
# inconsistency of Selenium expected_conditions behavior with Amazon.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys
import traceback
import config
from time import sleep
import pdb

class AmazonProductFinder():
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
        
        self.web_driver.get(website_url)
        self.wait = WebDriverWait(self.web_driver, 20)

    def userLogin(self):
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

    def searchForProduct(self):
        """Search for the product that was specified in the user prompt"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='twotabsearchtextbox']"))).send_keys(
            self.product_search, Keys.ENTER)

    def adjustSortOrder(self):
        """Adjust search filter to filter by highest average review"""
        sleep(5)
        self.web_driver.find_element(By.XPATH,
            "//*[@id='a-autoid-0-announce']").click()
        self.web_driver.find_element(By.XPATH,
            "//*[@id='s-result-sort-select_3']").click()

    def goToProductPage(self):
        """Click on first result for product page"""
        self.wait.until(ec.element_to_be_clickable((By.XPATH,
            "//*[@data-cel-widget='search_result_1']//img"))).click()
        
    def addProductToCart(self):
        """Add product to cart and decline extended warranty if present"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='submit.add-to-cart']"))).click()
        sleep(5)
        self.declineWarrantyOffer()

    # Amazon does not always present warranty dialogue for all products
    # Javascript neccessary as there is a Selenium bug with modal interactions
    def declineWarrantyOffer(self):
        """Decline warranty offer pop up"""
        try:
            decline_warranty_offer = self.web_driver.find_element(By.XPATH,
                "/html/body/div[4]/div/div/header/button")
            self.web_driver.execute_script("arguments[0].click();",
                decline_warranty_offer)
        except NoSuchElementException:
            pass

    def goToCart(self):
        """Navigate to shopping cart"""
        self.wait.until(ec.element_to_be_clickable((By.XPATH,
            "//*[@id='hlb-view-cart-announce']"))).click()
            
    def closeBrowserWindow(self):
        """Issue quit against web driver object"""
        self.web_driver.quit()