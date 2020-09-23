    #!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out Firefox class
# TODO: Build out Safari class
# TODO: Build out test framework with pytest
# TODO: Make sure rogue chrome processes are killed on host machine
# TODO: Possibly remove self prefix from web driver variable(s)
# TODO: Split up classes into different modules?
# TODO: Convert user login to xpath

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import config

def userPrompt():
    """Prompt user to search for a product. Return product"""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please input a product to search for, and amazon product finder "
        "will automagically\nfind the highest rated product of your search "
        "and add it to the shopping cart."
    )
    product_search = input("Product search: ")
    return product_search

class ChromeAmazonProductFinder():
    def __init__ (self, product_search):
        """
        Create Selenium driver object and open up Amazon.com on Chrome
        Execute class methods to search for, find and add the product to cart
        """
        self.product_search = product_search
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(chrome_options=options)
        self.chrome_driver.get('https://amazon.com')
        sleep(3)
        self.searchForProduct()
        self.adjustSearchFilter()
        self.goToProductPage()
        self.addProductToCart()
        self.goToCart()

    def userLogin(self):
        """
        Log into amazon. This method is temporarily deprecated as logging in
        via Selenium requires granting authentication permission via email
        """
        hello_sign_in_button = self.chrome_driver.find_element_by_css_selector(
            "#nav-link-accountList").click()
        email_address_field = self.chrome_driver.find_element_by_name("email")
        email_address_field.send_keys(config.USERNAME)
        continue_button = self.chrome_driver.find_element_by_css_selector(
            "#continue").click()
        password_field = self.chrome_driver.find_element_by_name("password")
        password_field.send_keys(config.PASSWORD)
        password_button = self.chrome_driver.find_element_by_css_selector(
            "#signInSubmit").click()
        sleep(1)            

    def searchForProduct(self):
        """Search for the product that was specified in the user prompt"""
        search_bar = self.chrome_driver.find_element(
            By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys(
            self.product_search, Keys.ENTER)
        self.chrome_driver.implicitly_wait(5)

    def adjustSearchFilter(self):
        """Adjust search filter to filter by highest average review"""
        adjust_filter = self.chrome_driver.find_element(
            By.XPATH, "//*[@id='a-autoid-0-announce']").click()
        self.chrome_driver.implicitly_wait(5)
        sort_by_rating = self.chrome_driver.find_element(
            By.XPATH, "//*[@id='s-result-sort-select_3']").click()        

    def goToProductPage(self):
        """Click on first result for product page"""
        go_to_product_page = self.chrome_driver.find_element(
            By.XPATH, "//div[@data-cel-widget='search_result_1']//img").click()
        self.chrome_driver.implicitly_wait(5)
        
    def addProductToCart(self):
        """Add product to cart and decline extended warranty if present"""
        add_to_cart = self.chrome_driver.find_element(
            By.XPATH, "//*[@id='submit.add-to-cart']").click()
        try:
            decline_protection_plan = self.chrome_driver.find_element(
                By.XPATH, "//*[@id='siNoCoverage-announce']")
            self.chrome_driver.execute_script(
                "arguments[0].click();", decline_protection_plan)
        except NoSuchElementException:
            pass

    def goToCart(self):
        """Navigate to shopping cart"""
        go_to_cart = self.chrome_driver.find_element(
            By.XPATH, "//*[@id='hlb-view-cart-announce']").click()


class FirefoxAmazonProductFinder():
    def __init__ (self, product_search):
        self.product_search = product_search
        self.firefox_driver = webdriver.Firefox()
        self.firefox_driver.get('https://amazon.com')

    def userLogin(self):
        pass

    def searchForProduct(self):
        pass

    def adjustSearchFilter(self):
        pass

    def goToProductPage(self):
        pass
    
    def addProductToCart(self):
        pass

    def __str__(self):
        pass


class SafariAmazonProductFinder():
    def __init__ (self, product_search):
        self.product_search = product_search        

    def userLogin(self):
        pass

    def searchForProduct(self):
        pass

    def adjustSearchFilter(self):
        pass

    def goToProductPage(self):
        pass
    
    def addProductToCart(self):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    # product_search = userPrompt()
    # chrome_browser = ChromeAmazonProductFinder(product_search)

    product_search = 'electric water kettle'
    firefox_browser = FirefoxAmazonProductFinder(product_search)