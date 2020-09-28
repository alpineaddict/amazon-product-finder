"""
Chrome automation for Amazon product search and find.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import config

class ChromeAmazonProductFinder():
    def __init__ (self, website_url, product_search):
        """
        Create Selenium driver object and open up Amazon.com on Chrome
        Execute class methods to search for, find and add the product to cart
        """
        self.product_search = product_search
        self.website_url = website_url
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(chrome_options=options)
        self.chrome_driver.get(website_url)
        self.wait = WebDriverWait(self.chrome_driver, 20)

    def userLogin(self):
        """
        Log into amazon. This method is unused for now as logging in
        via Selenium requires granting authentication permission via email
        """
        self.chrome_driver.find_element(By.XPATH,
            "//*[@id='nav-link-accountList']").click()        
        self.chrome_driver.find_element(
            By.XPATH, "//*[@id='ap_email']").send_keys(config.USERNAME,
            Keys.ENTER)
        self.chrome_driver.find_element(By.XPATH, 
            "//*[@id='ap_password']").send_keys(config.PASSWORD, Keys.ENTER)

    def searchForProduct(self):
        """Search for the product that was specified in the user prompt"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='twotabsearchtextbox']"))).send_keys(
            self.product_search, Keys.ENTER)

    def adjustSearchFilter(self):
        """Adjust search filter to filter by highest average review"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='a-autoid-0-announce']"))).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
             "//*[@id='s-result-sort-select_3']"))).click()

    def goToProductPage(self):
        """Click on first result for product page"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//div[@data-cel-widget='search_result_1']//img"))).click()
        
    def addProductToCart(self):
        """Add product to cart and decline extended warranty if present"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='submit.add-to-cart']"))).click()        
        # Amazon does not always present warranty dialogue for all products
        try:
            decline_protection_plan = self.chrome_driver.find_element(
                By.XPATH, "//*[@id='siNoCoverage-announce']")
            self.chrome_driver.execute_script(
                "arguments[0].click();", decline_protection_plan)
        except NoSuchElementException:
            pass

    def goToCart(self):
        """Navigate to shopping cart"""
        self.wait.until(ec.visibility_of_element_located((By.XPATH,
            "//*[@id='hlb-view-cart-announce']"))).click()