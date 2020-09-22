    #!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out Chrome class
# TODO: Build out Firefox class
# TODO: Build out Safari class
# TODO: Build out test framework with pytest
# TODO: Make sure rogue chrome processes are killed
# TODO: Possibly remove self prefix from web driver variable(s)
# TODO: combine search and find key lines?
# TODO: combine all of the class methods into one that does everything

#   Script workflow
# - Prompt user for product search
# - Open up web browser(s)
# - Navigate to amazon
# - Log in
# - Search for product
# - Adjust filter
# - Add item to cart

import os
import requests   # might not need this?
from selenium import webdriver
from time import sleep
import config

def userPrompt():
    """Prompt user to search for a product. Return product."""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please input a product to search for, and amazon product finder "
        "will automagically\nfind the highest rated product of your search "
        "and add it to the shopping cart."
    )
    product_search = input("Product search: ")
    return product_search

class AmazonSearchAndFindProductForChrome():
    def __init__ (self, product_search):
        """Create Selenium driver object and open up Amazon.com on Chrome"""
        self.product_search = product_search
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(chrome_options=options)
        self.chrome_driver.get('https://amazon.com')
        sleep(1)        

    def userLogin(self):
        """
        Log into amazon. This method is temporarily deprecated as logging in
        via Selenium requires granting authentication permission via email.
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
        """Search for the product that was specified in the user prompt."""
        search_bar = self.chrome_driver.find_element_by_id("twotabsearchtextbox")
        search_bar.send_keys(self.product_search)
        search_button = self.chrome_driver.find_element_by_id(
            "nav-search-submit-text").click()
        sleep(1)

    def adjustSearchFilter(self):
        adjust_filter = self.chrome.find_element_by_css_selector(
            "#a-autoid-0-announce > span.a-dropdown-prompt").click()
        sort_by_rating = self.chrome.find_element_by_css_selector(
            "#s-result-sort-select_3").click()
        sleep(1)

    def goToProductPage(self):
        search_result = self.chrome.find_element_by_xpath(
            "//div[@data-cel-widget='search_search_result']//img").click()
        sleep(1)
        
    def addProductToCart(self):
        pass

    def __str__(self):
        pass


class AmazonSearchAndFindProductForFirefox():
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


class AmazonSearchAndFindProductForSafari():
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
    product_search = userPrompt()
    chrome_browser = AmazonSearchAndFindProductForChrome(product_search)
    # chrome_browser.userLogin()
    chrome_browser.searchForProduct()
    chrome_browser.adjustSearchFilter()
    chrome_browser.goToProductPage()
