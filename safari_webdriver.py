"""
Safari automation for Amazon product search and find.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import config

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